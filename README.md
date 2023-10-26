# Generative AI-Powered Token Classification Application with DistilBERT

This GitHub repository contains a Generative AI-powered application that uses an open-source language model (LLM) called DistilBERT, fine-tuned with the WNUT 17 database to perform Token Classification using Named Entity Recognition (NER). The repository also includes a Streamlit application that serves users who want to classify text they enter. Users can input text in a text box and click "Generate" to view the annotated output.

## Table of Contents
- [Requirements](#requirements)
- [Application Structure](#application-structure)
- [Usage](#usage)
- [Training the Model](#training-the-model)
- [Contributing](#contributing)
- [License](#license)

## Requirements

Packages used for this project can be found in [requirements.txt](/requirements.txt) Before using the application and training the model, ensure you have the following dependencies installed:

- [`transformers`](https://github.com/huggingface/transformers): This library is used for working with DistilBERT and fine-tuning it on the WNUT 17 dataset.
- [`st-annotated-text`](https://github.com/streamlit/st-annotated-text): Required for displaying the annotated text in the Streamlit application.
- [`huggingface-hub`](https://huggingface.co/): Used to access the DistilBERT model from the Hugging Face model hub.
- [`torch`](https://pytorch.org/): The deep learning backend for the transformers library.
- [`streamlit`](https://streamlit.io/): Used for creating the user-friendly web application.

You can install these requirements using pip:

```bash
pip install transformers st-annotated-text torch streamlit
```

## Application Structure

In this section, we provide an overview of the organization of files and folders in the repository:

- The [`app`](/app/) directory contains the code for the Streamlit application, with the following components:
  - [`app.py`](/app/app.py): This file contains the main code for the Streamlit application, which allows users to input text and view the annotated output.
  - [`utils.py`](/app/utils.py): Here, you can find various helper functions used in the application for tasks such as data preprocessing.
  - [`constants.py`](/app/constants.py): This file stores global constants and configurations that the application relies on.

- [`training_distilbert_wnut.ipynb`](/training_distilbert_wnut.ipynb): This Jupyter notebook is used for training the DistilBERT model on your data. It leverages the transformers library and PyTorch as the backend for model training.

This structured organization makes it easier to navigate the repository and locate specific components of the application and model training process.

## Training the Model

The raw [DistilBERT model](https://huggingface.co/distilbert-base-uncased) was trainined on the [WNUT 17](https://huggingface.co/datasets/wnut_17) database. A Jupyter notebook ([training_distilbert_wnut.ipynb](/training_distilbert_wnut.ipynb)) was setup to train the model. Make sure the required dependencies have been installed before running the notebook.

| The trained model can also be accessed on my huggingface repo: [neelgokhale/distilbert-finetuned-ner](https://huggingface.co/neelgokhale/distilbert-finetuned-ner)

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository to your GitHub account.
2. Create a new branch for your feature or bug fix:
```bash
git checkout -b feature-name
```
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your branch on GitHub:
```bash
git push origin feature-name
```
5. Create a pull request from your branch to the main repository.