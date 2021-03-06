import re
import typing
from typing import Any, Optional, Text, Dict

from rasa.nlu.components import Component


if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


class WikipediaAPI(Component):
    '''Composant de détection de l'action de recherche wikipédia, permet de :
    - passer outre les processus précédents et 
    - déclencher une requête API aux servers wikipédia dans le cas où le message utilisateur satisfait la regex.
    '''

    # attributs de classe
    provides = ["intent", "entities"]
    requires = ["intent", "entities"]
    defaults = {}
    language_list = None # matche toutes les langues

    def __init__(self, component_config=None):
        '''Méthode d'instanciation :
        - matche uniquement les messages qui commencent par "wikepdia:" en ignorant les espaces,
        - de nouveaux mots peuvent être ajoutés ici mais ce n'est pas conseillé afin de minimiser les risques de collisions entre la détection d'intent NLP et la reconnaissance par mots-clés.
        '''

        super().__init__(component_config)

        # attributs d'instance
        self.pattern = r"^\s*(?P<wiki_trigger>(wikipedia:)|(wikipédia:))\s*(?P<wiki_phrase>.+)"
        self.compiled = re.compile(self.pattern, flags = re.IGNORECASE)

    def train(self, training_data, cfg, **kwargs):
        '''Méthode d'entrainement - inutile ici.'''
        pass

    def process(self, message, **kwargs):
        text = message.text
        result = self.compiled.search(text)
        if not result:
          return
        else:
          s_phrase = result.group("wiki_phrase")
          start, end = result.span(2)
          sphr_entity = {
            "start": start,
            "end": end,
            "value": s_phrase,
            "entity": "wiki_phrase",
            "extractor": "WikipediaAPI",
            "confidence": 1.0,
            "processors": []
            }
          intent = {"name": "wikipedia", "confidence": 1.0}
          intent_ranking = [
            {
            "confidence": 1.0,
            "name": "wikipedia"
            }
            ]
          
          message.set("intent", intent, add_to_output = True)
          message.set("intent_ranking", intent_ranking)
          message.set("entities", [sphr_entity], add_to_output=True)
        
    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """Charge ce composant d'un fichier."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
