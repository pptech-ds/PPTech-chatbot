import logging
import os
import random

import numpy as np
import torch
from torch.utils.data import (DataLoader, SequentialSampler,TensorDataset)
from torch.utils.data.distributed import DistributedSampler
from tqdm import tqdm

from .modeling_bert_local import (WEIGHTS_NAME, BertConfig, BertForSequenceClassification)

from .tokenization_bert_local import (BertTokenizer)

from .utils_glue import (compute_metrics, convert_examples_to_features, output_modes, processors)

from .modeling_bert_local import (BERT_PRETRAINED_MODEL_ARCHIVE_MAP, BERT_PRETRAINED_CONFIG_ARCHIVE_MAP)

logger = logging.getLogger(__name__)

# ALL_MODELS = 'bert-base-uncased'

# MODEL_CLASSES = {
#     'bert': (BertConfig, BertForSequenceClassification, BertTokenizer)
# }


def set_seed(arg_dict):
    random.seed(42)
    np.random.seed(42)
    torch.manual_seed(42)
    



def predict(arg_dict, model, tokenizer, dict_classifier, prefix=""):
    # Loop to handle MNLI double evaluation (matched, mis-matched)
    eval_task_names = ("mnli", "mnli-mm") if arg_dict['task_name'] == "mnli" else (arg_dict['task_name'],)
    eval_outputs_dirs = (arg_dict['model_path'], arg_dict['model_path'] + '-MM') if arg_dict['task_name'] == "mnli" else (arg_dict['model_path'],)

    predict_dict = {}
    predict_dict['pred_binary_val'] = []
    predict_dict['pred_explicit_val'] = []
    predict_dict['expected_binary_val'] = []
    predict_dict['expected_explicit_val'] = []
    # predict_dict['BM25_score'] = []
    #predict_dict['seed_id'] = []
    predict_dict['seed_label'] = []
    predict_dict['seed_value'] = []

    local_rank = -1

    results = {}
    for eval_task, eval_output_dir in zip(eval_task_names, eval_outputs_dirs):
        eval_dataset = load_predict_data(arg_dict, eval_task, tokenizer, dict_classifier, evaluate=True)

        if not os.path.exists(eval_output_dir) and local_rank in [-1, 0]:
            os.makedirs(eval_output_dir)

        #for i in range(len(dict_classifier['seed_url'])):
        #    print('seed_url[{}]: {} '.format(i, dict_classifier['seed_url'][i]))

        arg_dict['eval_batch_size'] = arg_dict['per_gpu_eval_batch_size'] * max(1, arg_dict['n_gpu'])
        # Note that DistributedSampler samples randomly
        eval_sampler = SequentialSampler(eval_dataset) if local_rank == -1 else DistributedSampler(eval_dataset)
        eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=arg_dict['eval_batch_size'])

        # Eval!
        #logger.info("***** Running evaluation {} *****".format(prefix))
        #logger.info("  Num examples = %d", len(eval_dataset))
        #logger.info("  Batch size = %d", args.eval_batch_size)
        eval_loss = 0.0
        nb_eval_steps = 0
        preds = None
        out_label_ids = None
        for batch in tqdm(eval_dataloader, desc="Evaluating"):
            model.eval()
            batch = tuple(t.to(arg_dict['device']) for t in batch)

            with torch.no_grad():
                inputs = {'input_ids':      batch[0],
                          'attention_mask': batch[1],
                          'token_type_ids': batch[2] if arg_dict['model_type'] in ['bert', 'xlnet'] else None,  # XLM and RoBERTa don't use segment_ids
                          'labels':         batch[3]}
                outputs = model(**inputs)
                #logger.info("line368::outputs: {} ".format(outputs))
                #logger.info("line369::outputs[:2]: {} ".format(outputs[:2]))

                tmp_eval_loss, logits = outputs[:2]
                

                eval_loss += tmp_eval_loss.mean().item()
            nb_eval_steps += 1
            if preds is None:
                preds = logits.detach().cpu().numpy()
                out_label_ids = inputs['labels'].detach().cpu().numpy()
            else:
                preds = np.append(preds, logits.detach().cpu().numpy(), axis=0)
                out_label_ids = np.append(out_label_ids, inputs['labels'].detach().cpu().numpy(), axis=0)
            
            #logger.info("In predict::preds: {} ".format(preds))
            #logger.info("In predict::out_label_ids: {} ".format(out_label_ids))

        eval_loss = eval_loss / nb_eval_steps
        if arg_dict['output_mode'] == "classification":
            preds = np.argmax(preds, axis=1)
        elif arg_dict['output_mode'] == "regression":
            preds = np.squeeze(preds)
        result = compute_metrics(eval_task, preds, out_label_ids)
        results.update(result)

        torch.set_printoptions(profile="full")
        #logger.info("In predict::preditions: {} ".format(preds))
        #logger.info("In predict::input labels: {} ".format(out_label_ids))
        torch.set_printoptions(profile="default")

        for i in range(len(preds)):
            predict_dict['pred_binary_val'].append(preds[i])
            predict_dict['expected_binary_val'].append(out_label_ids[i])
            # predict_dict['BM25_score'].append(dict_classifier['BM25_score'][i])
            #print('i in predict = {}'.format(i))
            #predict_dict['seed_id'].append(dict_classifier['seed_id'][i])
            predict_dict['seed_label'].append(dict_classifier['label'][i])
            predict_dict['seed_value'].append(dict_classifier['sentence'][i])

            if(preds[i]==0):
                predict_dict['pred_explicit_val'].append('True')
            else:
                predict_dict['pred_explicit_val'].append('False')
            
            if(out_label_ids[i]==0):
                predict_dict['expected_explicit_val'].append('True')
            else:
                predict_dict['expected_explicit_val'].append('False')
        

        output_eval_file = os.path.join(eval_output_dir, "eval_results.txt")
        with open(output_eval_file, "w") as writer:
            #logger.info("***** Eval results {} *****".format(prefix))
            for key in sorted(result.keys()):
                #logger.info("  %s = %s", key, str(result[key]))
                writer.write("%s = %s\n" % (key, str(result[key])))

    return (results, predict_dict)




def load_predict_data(arg_dict, task, tokenizer, dict_classifier, evaluate=False):

    local_rank = -1

    if local_rank not in [-1, 0] and not evaluate:
        torch.distributed.barrier()  # Make sure only the first process in distributed training process the dataset, and the others will use the cache

    processor = processors[task]()
    output_mode = output_modes[task]
    # Load data features from cache or dataset file
    
    #logger.info("Creating features from dataset file at %s", args.data_dir)
    label_list = processor.get_labels()
    

    examples = processor.get_examples(dict_classifier)
    #exit()
    #print('examples in load_predict_data: {} '.format(examples))
    features = convert_examples_to_features(examples, label_list, arg_dict['max_seq_length'], tokenizer, output_mode,
        cls_token_at_end=bool(arg_dict['model_type'] in ['xlnet']),            # xlnet has a cls token at the end
        cls_token=tokenizer.cls_token,
        cls_token_segment_id=2 if arg_dict['model_type'] in ['xlnet'] else 0,
        sep_token=tokenizer.sep_token,
        sep_token_extra=bool(arg_dict['model_type'] in ['roberta']),           # roberta uses an extra separator b/w pairs of sentences, cf. github.com/pytorch/fairseq/commit/1684e166e3da03f5b600dbb7855cb98ddfcd0805
        pad_on_left=bool(arg_dict['model_type'] in ['xlnet']),                 # pad on the left for xlnet
        pad_token=tokenizer.convert_tokens_to_ids([tokenizer.pad_token])[0],
        pad_token_segment_id=4 if arg_dict['model_type'] in ['xlnet'] else 0,
    )

    #print('features in load_predict_data: {} '.format(features))

    '''
    for f in features:
        print('f.input_ids: {} '.format(f.input_ids))
        print('f.input_mask: {} '.format(f.input_mask))
        print('f.segment_ids: {} '.format(f.segment_ids))
        print('f.label_id: {} '.format(f.label_id))
    '''

    if local_rank == 0 and not evaluate:
        torch.distributed.barrier()  # Make sure only the first process in distributed training process the dataset, and the others will use the cache

    # Convert to Tensors and build dataset
    all_input_ids = torch.tensor([f.input_ids for f in features], dtype=torch.long)
    all_input_mask = torch.tensor([f.input_mask for f in features], dtype=torch.long)
    all_segment_ids = torch.tensor([f.segment_ids for f in features], dtype=torch.long)
    if output_mode == "classification":
        all_label_ids = torch.tensor([f.label_id for f in features], dtype=torch.long)
    elif output_mode == "regression":
        all_label_ids = torch.tensor([f.label_id for f in features], dtype=torch.float)

    dataset = TensorDataset(all_input_ids, all_input_mask, all_segment_ids, all_label_ids)

    # print('dataset: {}  '.format(dataset))

    return dataset


def qsc(arg_dict, dict_classifier):
    
    local_rank = -1

    # Setup CUDA, GPU & distributed training
    if local_rank == -1:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        arg_dict['n_gpu'] = torch.cuda.device_count()

    arg_dict['device'] = device

    # Setup logging
    logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                        datefmt = '%m/%d/%Y %H:%M:%S',
                        level = logging.INFO if local_rank in [-1, 0] else logging.WARN)
    logger.warning("Process rank: %s, device: %s, distributed training: %s, 16-bits training: %s",
                    local_rank, device, bool(local_rank != -1), '')

    # Set seed
    set_seed(arg_dict)

    # Prepare GLUE task
    arg_dict['task_name'] = arg_dict['task_name'].lower()
    if arg_dict['task_name'] not in processors:
        raise ValueError("Task not found: %s" % (arg_dict['task_name']))
    processor = processors[arg_dict['task_name']]()
    arg_dict['output_mode'] = output_modes[arg_dict['task_name']]
    label_list = processor.get_labels()
    num_labels = len(label_list)

    # Load pretrained model and tokenizer
    if local_rank not in [-1, 0]:
        torch.distributed.barrier()  # Make sure only the first process in distributed training will download model & vocab

    arg_dict['model_type'] = arg_dict['model_type'].lower()
    config_class, model_class, tokenizer_class = MODEL_CLASSES[arg_dict['model_type']]
    config = config_class.from_pretrained('' if '' else arg_dict['model_name_or_path'], num_labels=num_labels, finetuning_task=arg_dict['task_name'])
    #tokenizer = tokenizer_class.from_pretrained('' if '' else args.model_name_or_path, do_lower_case=args.do_lower_case)
    tokenizer = tokenizer_class.from_pretrained('' if '' else arg_dict['model_name_or_path'], do_lower_case=True)
    model = model_class.from_pretrained(arg_dict['model_name_or_path'], from_tf=bool('.ckpt' in arg_dict['model_name_or_path']), config=config)

    if local_rank == 0:
        torch.distributed.barrier()  # Make sure only the first process in distributed training will download model & vocab

    model.to(arg_dict['device'])

    # Prediction
    results = {}
    predict_dict = {}
    
    #tokenizer = tokenizer_class.from_pretrained(args.output_dir, do_lower_case=args.do_lower_case)
    tokenizer = tokenizer_class.from_pretrained(arg_dict['model_path'], do_lower_case=True)
    checkpoints = [arg_dict['model_path']]
    
    for checkpoint in checkpoints:
        global_step = checkpoint.split('-')[-1] if len(checkpoints) > 1 else ""
        model = model_class.from_pretrained(checkpoint)
        model.to(arg_dict['device'])
        #logger.info("Doing prediction ...")
        (result, predict_dict) = predict(arg_dict, model, tokenizer, dict_classifier, prefix=global_step)
        result = dict((k + '_{}'.format(global_step), v) for k, v in result.items())
        results.update(result)

        '''
        for key in predict_dict:
            logger.info("Values for predict_dict[{}]: {} ".format(key, predict_dict[key]))
        '''
        
    return predict_dict




def load_model(arg_dict):
    # Set seed
    set_seed(arg_dict)

    # Prepare GLUE task
    arg_dict['task_name'] = arg_dict['task_name'].lower()
    if arg_dict['task_name'] not in processors:
        raise ValueError("Task not found: %s" % (arg_dict['task_name']))
    processor = processors[arg_dict['task_name']]()
    arg_dict['output_mode'] = output_modes[arg_dict['task_name']]
    label_list = processor.get_labels()
    num_labels = len(label_list)

    # BERT
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased-skillogs', do_lower_case=True, do_basic_tokenize=True)
    model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-uncased-skillogs')
    model.to(arg_dict['device'])


    return (model, tokenizer)




def predict_ontime(arg_dict, model, tokenizer, dict_classifier, prefix=""):
    
    predict_dict = {}
    predict_dict['pred_binary_val'] = []
    predict_dict['pred_explicit_val'] = []
    predict_dict['expected_binary_val'] = []
    predict_dict['expected_explicit_val'] = []
    # predict_dict['BM25_score'] = []
    predict_dict['seed_label'] = []
    predict_dict['seed_value'] = []

    local_rank = -1

    eval_dataset = load_predict_data(arg_dict, arg_dict['task_name'], tokenizer, dict_classifier, evaluate=True)

    # if not os.path.exists(arg_dict['output_dir']) and local_rank in [-1, 0]:
    #     os.makedirs(arg_dict['output_dir'])

    arg_dict['eval_batch_size'] = arg_dict['per_gpu_eval_batch_size'] * max(1, arg_dict['n_gpu'])
    # Note that DistributedSampler samples randomly
    eval_sampler = SequentialSampler(eval_dataset) if local_rank == -1 else DistributedSampler(eval_dataset)
    eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=arg_dict['eval_batch_size'])

    # Eval!
    #logger.info("***** Running evaluation {} *****".format(prefix))
    #logger.info("  Num examples = %d", len(eval_dataset))
    #logger.info("  Batch size = %d", args.eval_batch_size)
    eval_loss = 0.0
    nb_eval_steps = 0
    preds = None
    out_label_ids = None
    for batch in tqdm(eval_dataloader, desc="Evaluating"):
        model.eval()
        batch = tuple(t.to(arg_dict['device']) for t in batch)

        with torch.no_grad():
            inputs = {'input_ids':      batch[0],
                        'attention_mask': batch[1],
                        'token_type_ids': batch[2] if arg_dict['model_type'] in ['bert', 'xlnet'] else None,  # XLM and RoBERTa don't use segment_ids
                        'labels':         batch[3]}
            outputs = model(**inputs)
            tmp_eval_loss, logits = outputs[:2]
            eval_loss += tmp_eval_loss.mean().item()
        nb_eval_steps += 1

        if preds is None:
            preds = logits.detach().cpu().numpy()
            out_label_ids = inputs['labels'].detach().cpu().numpy()
        else:
            preds = np.append(preds, logits.detach().cpu().numpy(), axis=0)
            out_label_ids = np.append(out_label_ids, inputs['labels'].detach().cpu().numpy(), axis=0)
        
    eval_loss = eval_loss / nb_eval_steps
    if arg_dict['output_mode'] == "classification":
        preds = np.argmax(preds, axis=1)
    elif arg_dict['output_mode'] == "regression":
        preds = np.squeeze(preds)

    torch.set_printoptions(profile="full")
    torch.set_printoptions(profile="default")

    for i in range(len(preds)):
        predict_dict['pred_binary_val'].append(preds[i])
        predict_dict['expected_binary_val'].append(out_label_ids[i])
        # predict_dict['BM25_score'].append(dict_classifier['BM25_score'][i])
        predict_dict['seed_label'].append(dict_classifier['label'][i])
        predict_dict['seed_value'].append(dict_classifier['sentence'][i])

        if(preds[i]==0):
            predict_dict['pred_explicit_val'].append('True')
        else:
            predict_dict['pred_explicit_val'].append('False')
        
        if(out_label_ids[i]==0):
            predict_dict['expected_explicit_val'].append('True')
        else:
            predict_dict['expected_explicit_val'].append('False')
        

    return (predict_dict)