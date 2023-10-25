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
from constants import *
from utils import *


# SESSION STATE DECLARATIONS

if 'annot_text' not in st.session_state:
    st.session_state['annot_text'] = ''

# TITLE

st.set_page_config(
    page_title="GenAI App - Token Classifier",
    layout="wide"
)

with st.container():
    st.title("GenAI App - Token Classifier")
    st.divider()
    st.markdown(TITLE_TEXT)

# SIDEBAR

with st.sidebar:

    # HEADER - SIDEBAR
    st.header("Options")
    st.divider()

    # RADIO - MODEL SELECTION
    radio_model = st.radio(
        "Choose a **model**:",
        [i for i in MODELS],
        captions=CAPTIONS
    )

# MAIN

# INPUT CONTAINER

with st.container():
    with st.expander("Input Text"):
        input_text = st.text_area(
            label="",
            placeholder="Enter your text here...",
            label_visibility="collapsed"
        )

        if st.button("Generate", type="primary") and input_text:
            pred_labels = get_classification(
                input_text=input_text,
                model=radio_model
            )

            annot_tuple = get_annotated_classification(
                input_text=input_text,
                labels=pred_labels
            )
            

# OUTPUT CONTAINER
with st.container():
    with st.expander("Input Text"):
        annotated_text(
            annot_tuple
        )