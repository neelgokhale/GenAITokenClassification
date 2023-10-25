
# USER INFO

HUGGINGFACE_USER = "neelgokhale"

# MODELS

MODELS = ["distilbert-finetuned-ner", "model_2", "model_3"]
CAPTIONS = ["distilbert trained on WNUT 17 data", "add caption here", "add caption here"]

ID2LABEL = {
    "0": "O",
    "1": "B-corporation",
    "2": "I-corporation",
    "3": "B-creative-work",
    "4": "I-creative-work",
    "5": "B-group",
    "6": "I-group",
    "7": "B-location",
    "8": "I-location",
    "9": "B-person",
    "10": "I-person",
    "11": "B-product",
    "12": "I-product"
}

LABEL2ID = {
    "O": 0,
    "B-corporation": 1,
    "I-person": 10,
    "B-product": 11,
    "I-product": 12,
    "I-corporation": 2,
    "B-creative-work": 3,
    "I-creative-work": 4,
    "B-group": 5,
    "I-group": 6,
    "B-location": 7,
    "I-location": 8,
    "B-person": 9
}

# APP

TITLE_TEXT = \
"""
This application harnesses the power of fine-tuned Large Language Models (LLMs) to perform in token classification using Named Entity Recognition (NER). The application offers a few models, each trained on different sets of training data. The default model is a DistilBert LLM, that has been fine-tuned using the `WNUT_17` dataset.
"""