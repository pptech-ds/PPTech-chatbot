import requests
import csv
import pandas as pd
import string
from string import punctuation
import re
import json
import spacy

from modules.functions import ensureUtf
from modules.functions import clean_text
from modules.functions import tokenize_cleaned_text


# charge le profile utilisateur pour pouvoir acceder a la base de données
def load_user_config(user_config_json):
    with open(user_config_json, encoding='UTF-8') as json_file:
        user_config = json.load(json_file)
    
    return user_config
    

# requete de la base de données
def request_from_db(user_config_json, keywords_filter_list, knowledges_csv):
    # chargement du profil utilisateur
    user_config = load_user_config(user_config_json)

    APP_URL = user_config['API_URI'].replace('api','app')

    # authentification utilisateur
    res = requests.post(user_config['API_URI'] + '/auth/token', json={'email': user_config['API_USR'], 'password': user_config['API_PWD']})

    # verification si l'authentification utilisateur a bien fonctionné
    if res.status_code != 200:
        print('request::request_from_db: Error, not connected during POST')
        exit(1)

    # Store JWT Token in memory
    AuthHeader = {'Authorization': 'Bearer ' + res.json()['token']}

    df_knowledges = pd.read_csv(knowledges_csv, encoding='UTF-8', delimiter = ',')
    knowledge_id_list = ",".join(df_knowledges['knowledge_id'])

    requesting_string = user_config['API_URI'] + '/seeds?filter='+keywords_filter_list+'&page_size=1000&knowledge='+knowledge_id_list
    print('request::request_from_db: ligne de commande de la requete: {}\n'.format(requesting_string))

    # appelle API
    res = requests.get(requesting_string, headers=AuthHeader)
    if res.status_code != 200:
        print('request::request_from_db: An error occurred during GET')
        exit(1)

    res_json = res.json()
    #print(res_json)

    # construction du dictionnaire
    dict_result = {}
    dict_result['id'] = []
    dict_result['owner'] = []
    dict_result['label'] = []
    dict_result['value_original'] = []
    dict_result['value_clean_tokens'] = []
    dict_result['value_clean'] = []
    dict_result['type'] = []
    dict_result['duration'] = []
    dict_result['WatsonDocumentID'] = []
    dict_result['createdAt'] = []
    dict_result['updatedAt'] = []
    dict_result['seed_url'] = []

    for i in range(len(res_json['result'])):
        if(res_json['result'][i]['type'] == 'text/html'):
            dict_result['id'].append(res_json['result'][i]['id'])
            dict_result['owner'].append(res_json['result'][i]['owner'])
            dict_result['label'].append(res_json['result'][i]['label'])
            dict_result['value_original'].append(res_json['result'][i]['value'])
            # print('request::request_from_db: value_original: {}'.format(res_json['result'][i]['value']))
            value_clean_tokens = tokenize_cleaned_text(clean_text(res_json['result'][i]['value']))
            # print('request::request_from_db: value_clean_tokens: {}'.format(value_clean_tokens))
            dict_result['value_clean_tokens'].append(value_clean_tokens)
            value_clean = " ".join(value_clean_tokens)
            dict_result['value_clean'].append(value_clean)
            # print('request::request_from_db: value_clean: {}\n'.format(value_clean))
            dict_result['type'].append(res_json['result'][i]['type'])
            dict_result['duration'].append(res_json['result'][i]['duration'])
            dict_result['WatsonDocumentID'].append(res_json['result'][i]['WatsonDocumentID'])
            dict_result['createdAt'].append(res_json['result'][i]['createdAt'])
            dict_result['updatedAt'].append(res_json['result'][i]['updatedAt'])

            for j in range(len(df_knowledges['seed_id'])):
                if(df_knowledges['seed_id'][j]==res_json['result'][i]['id']):
                    seed_url = APP_URL+'/learn/'+df_knowledges['skill_id'][j]+'/knowledge/'+df_knowledges['knowledge_id'][j]+'/seed/'+df_knowledges['seed_id'][j]
                    dict_result['seed_url'].append(seed_url)
                            
    return dict_result


#Build knowledge_id list 
def build_knowledge_id_list(csv):
    df_knowledgeid = pd.read_csv(csv, delimiter = ',')
    knowledge_id_list = ",".join(df_knowledgeid['knowledge_id'])

    return knowledge_id_list





    
 