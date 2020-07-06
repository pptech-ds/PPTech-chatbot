import numpy as np
import pandas as pd
# import glob
import re
import csv

from rank_bm25 import BM25Okapi
# from nltk.corpus import stopwords 
# from nltk.tokenize import word_tokenize 
# from sklearn.cluster import KMeans
from modules.functions import ensureUtf
from modules.functions import clean_text
from modules.functions import tokenize_cleaned_text



#Build Corpus dictionnary to process BM25 Algo
def build_corpus_dict(result_dict):
    corpus_dict = {}
    corpus_dict['content'] = []
    corpus_dict['id'] = []
    corpus_dict['label'] = []
    corpus_dict['value_original'] = []
    corpus_dict['value_clean_tokens'] = []
    corpus_dict['value_clean'] = []
    corpus_dict['seed_url'] = []

    for i in range(len(result_dict['id'])):
        content = (' '.join(result_dict['value_clean_tokens'][i])) + ' ' + clean_text(result_dict['label'][i])
        #content = content.replace('"','')
        #content = content.replace("'","")
        content = content.strip()
        corpus_dict['content'].append(content)
        corpus_dict['id'].append(result_dict['id'][i])
        corpus_dict['label'].append(result_dict['label'][i])
        corpus_dict['value_original'].append(result_dict['value_original'][i])
        corpus_dict['value_clean_tokens'].append(result_dict['value_clean_tokens'][i])
        corpus_dict['value_clean'].append(result_dict['value_clean'][i])
        corpus_dict['seed_url'].append(result_dict['seed_url'][i])

    return corpus_dict



def bm25ranker(result_dict, keywords, BM25_threshold, tolerance, nb_max_result):
    
    corpus = build_corpus_dict(result_dict)

    dict_bm25ranker = {}
    dict_bm25ranker['tokenized_corpus'] = [doc.split(" ") for doc in corpus['content']]
    # print('bm25::bm25ranker: dict_bm25ranker[tokenized_corpus]: {}'.format(dict_bm25ranker['tokenized_corpus']))

    dict_bm25ranker['bm25'] = BM25Okapi(dict_bm25ranker['tokenized_corpus'])
    # print('bm25::bm25ranker: dict_bm25ranker[bm25]: {}'.format(dict_bm25ranker['bm25']))

    keywords = keywords.strip()
    dict_bm25ranker['tokenized_query'] = keywords.split(" ")
    # print('bm25::bm25ranker: dict_bm25ranker[tokenized_query]: {}'.format(dict_bm25ranker['tokenized_query']))

    dict_bm25ranker['doc_scores'] = dict_bm25ranker['bm25'].get_scores(dict_bm25ranker['tokenized_query'])
    # print('bm25::bm25ranker: dict_bm25ranker[doc_scores]: {}'.format(dict_bm25ranker['doc_scores']))

    dict_bm25ranker['top_n'] = dict_bm25ranker['bm25'].get_top_n(dict_bm25ranker['tokenized_query'], corpus['content'], n=100)
    # print('bm25::bm25ranker: dict_bm25ranker[top_n]: {}'.format(dict_bm25ranker['top_n']))
    # print('bm25::bm25ranker: corpus[content]: {}\n'.format(corpus['content']))


    dict_bm25ranker['id'] = []
    dict_bm25ranker['label'] = []
    dict_bm25ranker['value_original'] = []
    dict_bm25ranker['value_clean_tokens'] = []
    dict_bm25ranker['value_clean'] = []
    dict_bm25ranker['doc_scores_corpus'] = []
    dict_bm25ranker['sum_doc_scores_corpus'] = -1
    dict_bm25ranker['seed_url'] = []


    for i in range(len(dict_bm25ranker['top_n'])):
        for j in range(len(corpus['id'])):
            if(dict_bm25ranker['top_n'][i]==corpus['content'][j]):
                if(dict_bm25ranker['doc_scores'][j] > BM25_threshold):
                    dict_bm25ranker['id'].append(corpus['id'][j])
                    dict_bm25ranker['label'].append(corpus['label'][j])
                    dict_bm25ranker['value_original'].append(corpus['value_original'][j])
                    dict_bm25ranker['value_clean_tokens'].append(corpus['value_clean_tokens'][j])
                    dict_bm25ranker['value_clean'].append(corpus['value_clean'][j])
                    dict_bm25ranker['doc_scores_corpus'].append(dict_bm25ranker['doc_scores'][j])
                    dict_bm25ranker['seed_url'].append(corpus['seed_url'][j])


    
    dict_bm25ranker['sum_doc_scores_corpus'] = sum(dict_bm25ranker['doc_scores_corpus'])
    # print('bm25::bm25ranker: dict_bm25ranker[sum_doc_scores_corpus]: {}\n'.format(dict_bm25ranker['sum_doc_scores_corpus']))

    dict_bm25ranker['doc_scores_corpus_normalized'] = []

    
    if(dict_bm25ranker['sum_doc_scores_corpus'] != -1):
        for i in range(len(dict_bm25ranker['doc_scores_corpus'])):
            dict_bm25ranker['doc_scores_corpus_normalized'].append(dict_bm25ranker['doc_scores_corpus'][i]/dict_bm25ranker['sum_doc_scores_corpus'])
    else:
        print('Error in ranker!')
    
    # print('bm25::bm25ranker: dict_bm25ranker[doc_scores_corpus_normalized]: {}\n'.format(dict_bm25ranker['doc_scores_corpus_normalized']))


    # significant_values_list = get_significant_values(dict_bm25ranker['doc_scores_corpus_normalized'], tolerance)
    # print('bm25::bm25ranker: significant_values_list: {}\n'.format(significant_values_list))

    significant_values_list = dict_bm25ranker['doc_scores_corpus_normalized']

    dict_filtered_bm25ranker = {}
    dict_filtered_bm25ranker['label'] = []
    dict_filtered_bm25ranker['doc_scores_corpus_normalized'] = []
    dict_filtered_bm25ranker['seed_url'] = []
    dict_filtered_bm25ranker['value_clean'] = []

    for i in range(len(dict_bm25ranker['doc_scores_corpus_normalized'])):
        if(i == (nb_max_result)):
            break
        else:
            for j in range(len(significant_values_list)):
                if(dict_bm25ranker['doc_scores_corpus_normalized'][i] == significant_values_list[j]):
                    dict_filtered_bm25ranker['label'].append(dict_bm25ranker['label'][i])
                    dict_filtered_bm25ranker['doc_scores_corpus_normalized'].append(dict_bm25ranker['doc_scores_corpus_normalized'][i])
                    dict_filtered_bm25ranker['seed_url'].append(dict_bm25ranker['seed_url'][i])
                    joiner = ' '
                    # print('\nbm25ranker: dict_bm25ranker[value_clean_tokens][{}]: {}\n'.format(i, dict_bm25ranker['value_clean_tokens'][i]))
                    current_value_clean = joiner.join(dict_bm25ranker['value_clean_tokens'][i])
                    dict_filtered_bm25ranker['value_clean'].append(current_value_clean)
                    break



    return dict_filtered_bm25ranker



def get_significant_values(value_list, tolerance):

    #diff_list = []
    significant_value_list = []

    # for i in range(len(value_list)-1):
    for i in range(len(value_list)):
        if(len(value_list) > 1):
            current_diff = value_list[i] - value_list[i+1]

            if(i==0):
                if(current_diff < tolerance):
                    significant_value_list.append(value_list[i])
                    significant_value_list.append(value_list[i+1])
                else:
                    significant_value_list.append(value_list[i])
                    break
            else:
                if(current_diff < tolerance):
                    significant_value_list.append(value_list[i+1])
                else:
                    break
        else:
            significant_value_list.append(value_list[i])

    return significant_value_list


def gen_sentence_for_classifier(dict_bm25ranker, query):
    dict_classifier = {}
    dict_classifier['sentence'] = []
    dict_classifier['label'] = []
    dict_classifier['BM25_score'] = []
    dict_classifier['seed_url'] = []

    query_clean_tokens = tokenize_cleaned_text(clean_text(query))
    query_clean = " ".join(query_clean_tokens)
    print('gen_sentence_for_classifier: query: {}'.format(query))
    print('gen_sentence_for_classifier: query_clean: {}\n'.format(query_clean))

    for i in range(len(dict_bm25ranker['doc_scores_corpus_normalized'])):
        # print('\ngen_sentence_for_classifier: dict_bm25ranker[value_clean][{}]: {}\n'.format(i, dict_bm25ranker['value_clean'][i]))
        my_current_sentence = '[CLS] ' + query_clean + ' [SEP] ' + dict_bm25ranker['value_clean'][i]
        dict_classifier['sentence'].append(my_current_sentence)
        dict_classifier['label'].append(0)
        dict_classifier['BM25_score'].append(dict_bm25ranker['doc_scores_corpus_normalized'][i])
        dict_classifier['seed_url'].append(dict_bm25ranker['seed_url'][i])

    df = pd.DataFrame(dict_classifier) 

    return df


