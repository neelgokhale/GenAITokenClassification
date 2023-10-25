#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   app.py
@Time    :   2023/10/24 19:55:01
@Author  :   Neel Gokhale
@Contact :   neelg14@gmail.com
@License :   (C)Copyright 2020-2021, Neel Gokhale
'''

import os
import streamlit as st
from annotated_text import annotated_text

# VARS

MODELS = ["distilbert", "model_2", "model_3"]

# TITLE

st.title("GenAI App - Token Classifier")

# SIDEBAR

with st.sidebar:
    radio_model = st.radio(
        "Choose a `model`:",
        ["`" + i + "`" for i in MODELS],
        captions=[
            "distilbert trained on WNUT 17 data",
            "add caption here",
            "add caption here"
        ]
    )
    
# MAIN


