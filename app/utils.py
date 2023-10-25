#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   utils.py
@Time    :   2023/10/24 19:54:57
@Author  :   Neel Gokhale
@Contact :   neelg14@gmail.com
@License :   (C)Copyright 2020-2021, Neel Gokhale
'''

import os
import torch

from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from constants import *


def get_loaded_model(model: str):

    model_id = HUGGINGFACE_USER + "/" + model
    classifier = pipeline("ner", model=model_id)

    return classifier
    

def get_classification(input_text: str, model: str=MODELS[0]):

    model_id = HUGGINGFACE_USER + "/" + model

    # load tokenizer and generated tokenized list of response
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    input_tokens = tokenizer(input_text, return_tensors="pt")

    # load model
    model = AutoModelForTokenClassification.from_pretrained(model_id)
    with torch.no_grad():
        logits = model(**input_tokens).logits

    # get class with highest prob and use the model's id2label mapping
    preds = torch.argmax(logits, dim=2)
    pred_labels = [model.config.id2label[t.item()] for t in preds[0]]

    return pred_labels


def get_annotated_classification(input_text: str, labels: list):
    
    annot_tuple = []
    for txt, lbl in zip(input_text.split(" "), labels):
        annot_tuple.append((txt + " ", lbl))

    return annot_tuple


def get_classified_tokens_dict():
    pass
