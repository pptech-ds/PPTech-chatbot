# -*- coding: utf-8 -*-
import csv
import random
import logging
import requests
import numpy as np
from tqdm import tqdm
from typing import Text, Dict, Any, List

import torch
from torch.utils.data import (DataLoader, SequentialSampler,TensorDataset)
from torch.utils.data.distributed import DistributedSampler

from pytorch_transformers import (WEIGHTS_NAME, BertConfig, BertForSequenceClassification, BertTokenizer)

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused, FollowupAction

from modules.request_es import request_from_db
from modules.request_es import gen_sentence_for_classifier
from modules.qsc import qsc
from modules.qsc import load_model
from modules.qsc import predict_ontime
from modules.functions import build_keywords_list

logger = logging.getLogger(__name__)

# déclare les paramètres de l'IR dans un dict
arg_dict = {}
arg_dict['stopwords_csv'] = 'stopwords.csv'
# arg_dict['knowledges_csv'] = 'knowledges.csv'
arg_dict['model_type'] = 'bert'
arg_dict['model_name_or_path'] = 'bert-base-multilingual-uncased'
arg_dict['task_name'] = 'QSC'
arg_dict['max_seq_length'] = 512
arg_dict['output_dir'] = 'models/bert-base-multilingual-uncased-20191115-15h00'
arg_dict['per_gpu_eval_batch_size'] = 32
arg_dict['es_nb_max_result'] = 5
arg_dict['tolerance'] = 0.01
arg_dict['language'] = 'french'
arg_dict['user_config_json'] = 'user_config.json'
arg_dict['device'] = torch.device("cuda" if torch.cuda.is_available() else "cpu")
arg_dict['n_gpu'] = torch.cuda.device_count()
arg_dict['db_env'] = 'discovery_dev_clean'

# Setup logging
logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt = '%m/%d/%Y %H:%M:%S',
                    level = logging.INFO)
logger.warning("Process rank: %s, device: %s, distributed training: %s, 16-bits training: %s",
                -1, arg_dict['device'], bool(-1 != -1), '')


class ActionRechercher(Action):
    """ Fonction custom de recherche dans la base par l'intervention de deux modèles :
            - récupère l'input de l'utilisateur,
            - procède à un filtrage verbes-noms par spaCy,
            - requête le modèle d'Information Retrieving (IR) qui identifie les sources de réponse,
            - complété par le modèle de Reranking (Reranker) qui vérifie la pertinence des sources,
            - identifie les n premières propositions de réponse par un seuil de tolérance,
            - renvoie le résultat de la recherche à l'utilisateur.
    """

    def name(self):
        return "action_rechercher"

    def run(self, dispatcher, tracker, domain):
        # récupère l'intent et la requête du dernier message utilisateur
        intent = tracker.latest_message['intent'].get('name')
        query = (tracker.latest_message)['text']

        # ainsi que la valeur du slot booléen "relance"
        relance = tracker.get_slot("relance")
        
        # teste la valeur de l'intent ou du slot "relance"
        if intent == "recherche" or relance == True:

            # passe la requête au filtre des stopwords
            keywords_list = build_keywords_list(arg_dict['stopwords_csv'], arg_dict['language'], query)

            # requête Elasticsearch
            my_es_dict = request_from_db(keywords_list.strip(), arg_dict['db_env'])

            # teste si outputs non vides
            if len(keywords_list.strip()) > 1 and my_es_dict['seed_url']:
                # print debug classifier
                for i in range(len(my_es_dict['seed_url'])):
                    print('main:: my_es_dict[name][{}]: {} / my_es_dict[seed_url][{}]: {}\n'.format(i, my_es_dict['name'][i], i, my_es_dict['seed_url'][i]))

                # en déclarant les messages de retours qui seront sélectionnés au hasard
                retour = [
                    "Voilà ce que j'ai trouvé :",
                    "Voici quelques éléments de réponse :",
                    "Quelques pistes de réflexion :",
                    "Hop ! A toi de chercher là-dedans maintenant :"
                ]

                # en les concaténant tous dans un même message
                message = random.choice(retour)
                for i in range(min(len(my_es_dict['name']), arg_dict['es_nb_max_result'])):
                    message = message + '\n* [{}]({})'.format(
                            my_es_dict['name'][i],
                            my_es_dict['seed_url'][i]
                            )
                dispatcher.utter_message(message)

                # puis retourne le slot "recherche" à "reussie",
                # et retourne le slot "relance" à "False"
                return [
                    SlotSet("recherche", "reussie"),
                    SlotSet("relance", False),
                    UserUtteranceReverted()
                    ]
            else:
                # si non, renvoie un message d'échec
                dispatcher.utter_template("utter_recherche_echouee", tracker)

                # puis retourne le slot "recherche" à "echouee",
                # et retourne le slot "relance" à "False"
                return [
                    SlotSet("recherche", "echouee"),
                    SlotSet("relance", False),
                    UserUtteranceReverted()
                    ]
        
        # sinon retourne un message d'erreur (méthode "Raise" n'atteint pas l'utilisateur)
        else:
            return dispatcher.utter_message('Ah, j\'ai rencontré un problème système, je ne parviens pas à lancer ta recherche, essaie de la reformuler mais si le problème persiste, contacte un référent et transmet-lui le message suivant afin qu\'il me répare s\'il-te-plaît : "Erreur : intent >< \'recherche\' ET slot \'relance\' = False"')


class ActionDefaultFallback(Action):
    """ Fonction custom de fallback par défaut matérialisée par l'incompréhension du chatbot :
            - annule la dernière incompréhension pour ne pas impacter les prédictions futures,
            - force une action de recherche par défaut.
    """

    def name(self) -> Text:
        return "action_incomprehension"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List["Event"]:

        # retourne un message d'incompréhension à l'utilisateur indiquant le lancement d'une recherche par défaut
        dispatcher.utter_template("utter_incomprehension", tracker),

        # puis retourne le slot booléen "relance" à "True" 
        # et lance la fonction de recherche
        return [
            SlotSet("relance", True),
            FollowupAction("action_rechercher"),
            ]


class Conversation(Action):
    """Retourne le utter correspondant à l'intent conversationnel détecté."""

    def name(self):
        return "action_conversation"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")

        # récupère l'utter conversationnel correspondant à l'intent détecté
        if intent in [
            "saluer",
            "identite", 
            "insulter",
            "createur",
            "meteo",
            "possibilites",
            "isbot",
            "quel_age",
            "quelle_langue",
            "quelle_heure",
            "qui_suis_je",
            "quel_nom",
            "origine_lieu",
            "origine_construction",
            "faire_connaissance",
            "faire_blague",
            "quel_genre",
            "merci",
            "affirmer",
            "infirmer",
            "complimenter"
        ]:
            dispatcher.utter_template("utter_" + intent, tracker)
        return []


class TraductionAPI(Action):
    """Requête le traducteur skillogs avec la chaîne de caractères [STR] passée par l'utilisateur vers la [LANGUE] souhaitée par la commande : "translate_[LANGUE]: [STR]"\n
    Exemples : 
    - "translate_en: Comment vas-tu ?" passera la chaîne de caractères "Comment vas-tu ?" en paramètre de la requête API au traducteur_fr2en de Skillogs,
    - "translate_fr: How are you?" passera la chaîne de caractères "How are you?" en paramètre de la requête API au traducteur_en2fr de Skillogs.
    """

    # attributs de classe
    HOST = 'http://ec2-35-180-2-236.eu-west-3.compute.amazonaws.com'
    API_ENDPOINT = HOST + ":8080/"

    def name(self):
        return "action_traduction"
        
    def run(self, dispatcher, tracker, domain):

        # identification de la requête utilisateur
        user_input = tracker.latest_message['text']
        request_input = user_input[13:]

        # identification du sens de traduction souhaité
        if user_input[10:12] == 'fr':
            request_language = 'en2fr'
        elif user_input[10:12] == 'en':
            request_language = 'fr2en'
        else:
            raise ValueError("La langue de la traduction demandée n'est pas disponible")

        # construction des paramètres de la requête
        data = {'text2translate': request_input}
        url = self.API_ENDPOINT + request_language

        # execution de la requête
        request = requests.post(url = url, data = data)
        translation = request.text

        # retour vers l'utilisateur avec la chaîne de texte traduite
        output = "Voici ta traduction :\n" + translation
        dispatcher.utter_message(output)

        return [UserUtteranceReverted()]


class WikipediaAPI(Action):
    """Requête la base de donnée wikipédia avec le contenu de l'input utilisateur."""

    def name(self):
        return "action_wikipedia"

    def run(self, dispatcher, tracker, domain):

        # identification de la requête utilisateur
        user_input = tracker.latest_message['text']
        request_input = user_input[10:]

        # construction de la requête et de ses paramètres
        session = requests.Session()
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            'action'    : 'query',
            'format'    : 'json',
            'titles'    : request_input,
            'prop'      : 'info',
            'inprop'    : 'url|talkid'
        }

        # execution de la requête
        request = session.get(url=url, params=params)
        request_json = request.json()

        # identification du lien vers la recherche wikipédia
        result = {}
        for item in request_json['query']['pages'].items():
            result['titre'] = item[1]['title']
            result['lien'] = item[1]['fullurl']

        # retour vers l'utilisateur l'hyperlien de la recherche intégré dans le titre
        message = "Voici ce que dit Wikipédia :"
        output = message + '\n* [{}]({})'.format(
                result['titre'],
                result['lien']
                )
        dispatcher.utter_message(output)

        return [UserUtteranceReverted()]


class DefinitionAPI(Action):
    """Requête des API externes pour retourner des définitions de termes et concepts avec la chaîne de caractères [STR] passée par l'utilisateur à la suite du mot-clé : "define: [STR]"\n
    Exemple: "define: dyade" -> passera la chaîne de caractères "dyade" en paramètre de la requête API vers les dictionnaires externes.
    """

    def name(self):
        return "action_definition"

    def run(self, dispatcher, tracker, domain):
        return []