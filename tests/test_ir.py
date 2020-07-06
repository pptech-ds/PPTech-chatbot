# -*- coding: utf-8 -*-
import logging
from datetime import datetime
import json

import os
import random

import numpy as np
import torch
from torch.utils.data import (DataLoader, SequentialSampler,TensorDataset)
from torch.utils.data.distributed import DistributedSampler
from tqdm import tqdm

from pytorch_transformers import (WEIGHTS_NAME, BertConfig, BertForSequenceClassification, BertTokenizer)

from modules.request_es import request_from_db
from modules.request_es import gen_sentence_for_classifier
from modules.qsc import qsc
from modules.qsc import load_model
from modules.qsc import predict_ontime
from modules.functions import build_keywords_list
from modules.functions import replace_special_characters

# from modules.functions import build_keywords_list_spacy

logger = logging.getLogger(__name__)

# déclare les paramètres de l'IR dans un dict
arg_dict = {}
arg_dict['stopwords_csv'] = '../stopwords.csv'
arg_dict['model_type'] = 'bert'
arg_dict['model_name_or_path'] = 'bert-base-multilingual-uncased'
arg_dict['task_name'] = 'QSC'
arg_dict['max_seq_length'] = 512
arg_dict['model_path'] = 'https://skillogs1.s3.eu-west-3.amazonaws.com/skillogs-bert-20191115-15h00'
arg_dict['per_gpu_eval_batch_size'] = 32
arg_dict['BM25_threshold'] = 0
arg_dict['BM25_nb_max_result'] = 5
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


# (my_model, my_tokenizer) = load_model(arg_dict)


#run script until  end example 
query = ''

while(query!='exit'):
    query = input("Type something to test this out: ")
    print("main:: Ma requete: ", query)

    # passe la requête complète au filtre des stopwords
    keywords_list = build_keywords_list(arg_dict['stopwords_csv'], arg_dict['language'], query)

    print('main:: keywords_list {}'.format(keywords_list))

    # requête l'IR et récupère les outputs en base de la requête filtrée 
    my_es_dict = request_from_db(keywords_list.strip(), arg_dict['db_env'])

    # df = gen_sentence_for_classifier(my_es_dict, query)

    # print(df['seed_url'])

    # if(my_es_dict['name']):
    #     my_predict = predict_ontime(arg_dict, my_model, my_tokenizer, gen_sentence_for_classifier(my_es_dict, query), prefix="")
    #     for i in range(len(my_predict['pred_explicit_val'])):
    #         print('main:: my_predict[pred_explicit_val][{}]: {} / my_predict[seed_value][{}]: {}\n'.format(i, my_predict['pred_explicit_val'][i], i, my_predict['seed_value'][i]))

    for i in range(len(my_es_dict['seed_url'])):
        print('main:: my_es_dict[name][{}]: {} / my_es_dict[seed_url][{}]: {}\n'.format(i, my_es_dict['name'][i], i, my_es_dict['seed_url'][i]))
