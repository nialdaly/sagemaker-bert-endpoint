import torch
import os
import json
from transformers import BertTokenizer, BertForQuestionAnswering, BertConfig
import sys

JSON_CONTENT_TYPE = 'application/json'

def model_fn(model_dir):
    config_path = model_dir+'/config_file.json'
    model_path = model_dir+'/pytorch_model.bin'
    
    config = BertConfig.from_json_file(config_path)
    model = BertForQuestionAnswering(config)
    
    # Checks GPU state
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu')))
    return model

def input_fn(serialized_input_data, content_type=JSON_CONTENT_TYPE):
    if content_type == JSON_CONTENT_TYPE:
        input_data = json.loads(serialized_input_data)
        return input_data

    else:
        raise Exception('Requested unsupported ContentType in Accept: '+content_type)
        return

def predict_fn(input_data, model):
    vocab_path = '/opt/ml/model/vocab.txt'
    tokenizer = BertTokenizer(vocab_path, do_lower_case=True)

    question, context = input_data['question'], input_data['context']
    
    input_ids = tokenizer.encode(question, context)
    token_type_ids = [0 if i <= input_ids.index(102) else 1 for i in range(len(input_ids))]
    start_scores, end_scores = model(
        torch.tensor([input_ids]), 
        token_type_ids = torch.tensor([token_type_ids]))
    all_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    answer = ' '.join(all_tokens[torch.argmax(start_scores) : torch.argmax(end_scores)+1])
    return answer

def output_fn(prediction_output, accept=JSON_CONTENT_TYPE):
    if accept == JSON_CONTENT_TYPE:
        return json.dumps(prediction_output), accept
    
    raise Exception('Requested unsupported ContentType in Accept: '+accept)