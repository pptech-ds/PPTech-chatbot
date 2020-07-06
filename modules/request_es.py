import requests
import pandas as pd


# requete de la base de données
def request_from_db(keywords_filter_list, db_env):
    es_index = db_env # equivalent to SQL database
    # es_type = '_doc' # equivalent to SQL table: mandatory to use _doc for text elements

    # construction de la requête
    request_cmd_line = (
        'https://search-skillogs1-zrhgle3vemuqzhhs7fudth7cae.eu-west-3.es.amazonaws.com/'
        + es_index
        + '/_search?q='
        + keywords_filter_list
    )
    res = requests.get(request_cmd_line)

    # test du status de la requête
    if res.status_code != 200:
        # si mauvais status, message et sortie de boucle
        print('request_es::request_from_db: ERROR Elasticsearch requests.get({})'.format(request_cmd_line))
        # convention sortie de boucle en erreur
        exit(1)
    else:
        # sinon 
        print('request_es::request_from_db: Elasticsearch requests.get({})'.format(request_cmd_line))

    # déclaration du résultat de la requête en format json
    res_json = res.json()
    
    # déclaration du dictionnaire qui va servir à extraire les données souhaitées
    dict_result = {}
    dict_result['name'] = []
    dict_result['skill_id'] = []
    dict_result['knowledge_id'] = []
    dict_result['id'] = []
    dict_result['value'] = []
    dict_result['seed_url'] = []
    dict_result['score'] = []

    # extraction des données souhaitées
    for i in range(len(res_json['hits']['hits'])):
        if res_json['hits']['hits'][i]['_source']['id'] != '':
            dict_result['name'].append(res_json['hits']['hits'][i]['_source']['name'])
            dict_result['skill_id'].append(res_json['hits']['hits'][i]['_source']['skill_id'])
            dict_result['knowledge_id'].append(res_json['hits']['hits'][i]['_source']['knowledge_id'])
            dict_result['id'].append(res_json['hits']['hits'][i]['_source']['id'])
            dict_result['value'].append(res_json['hits']['hits'][i]['_source']['value'])
            dict_result['seed_url'].append(
                'https://dev.app.skillogs.com/learn/' 
                + str(res_json['hits']['hits'][i]['_source']['skill_id'])
                + '/knowledge/'
                + str(res_json['hits']['hits'][i]['_source']['knowledge_id'])
                + '/seed/'
                + str(res_json['hits']['hits'][i]['_source']['id'])
            )
            dict_result['score'].append(res_json['hits']['hits'][i]['_score'])

    # créé le dataframe des résultats de la requête
    df = pd.DataFrame(dict_result)

    # supprime les doublons par l'url des grains
    df.drop_duplicates(subset='seed_url', keep='first', inplace=True)
    df.reset_index(drop=True, inplace=True)

    # si moins de 3 grains filtrés
    if len(df) < 3:
        # retourne toutes les données filtrées par les doublons d'url
        return df.to_dict()

    # sinon
    else:
        # créé la colonne des moindres carrés
        df['least_squares'] = (df['score'] - df['score'].mean()) ** 2

        # identifie le coude
        elbow = min(df.least_squares)
        elbow_index = df[df.least_squares == elbow].index

        # sélectionne jusqu'au coude exclu
        df = df[df.index < elbow_index.tolist()[0]]

        # et retourne les données filtrées par le coude sur les moindres carrés
        return df.to_dict()


def gen_sentence_for_classifier(dict_es, query):
    dict_classifier = {}
    dict_classifier['sentence'] = []
    dict_classifier['label'] = []
    dict_classifier['seed_url'] = []

    # query_clean_tokens = tokenize_cleaned_text(clean_text(query))
    # query_clean = " ".join(query_clean_tokens)
    # print('gen_sentence_for_classifier: query: {}'.format(query))
    # print('gen_sentence_for_classifier: query_clean: {}\n'.format(query_clean))

    for i in range(len(dict_es['name'])):
        # print('\ngen_sentence_for_classifier: dict_es[value_clean][{}]: {}\n'.format(i, dict_es['value_clean'][i]))
        my_current_sentence = '[CLS] ' + query + ' [SEP] ' + dict_es['value'][i]
        dict_classifier['sentence'].append(my_current_sentence)
        dict_classifier['label'].append(0)
        dict_classifier['seed_url'].append(dict_es['seed_url'][i])

    df = pd.DataFrame(dict_classifier) 

    return df