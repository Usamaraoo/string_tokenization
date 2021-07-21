# pip install -U spacy
# python -m spacy download en_core_web_sm
from pathlib import Path
import random

from spacy.pipeline import ner
from tqdm import tqdm  # loading bar
import spacy

# Load English tokenizer, tagger, parser and NER
import os
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
# print(os.getcwd())
ner_model = None
output_dir = Path("/home/usama/Projects/Django/string tokenzation/Product-Named-Entity-Recognition/model1")
n_iter = 100
# Checks to see if there is a current model or no model. In this case I will be starting with a blank model

if ner_model is not None:
    ner_model = spacy.load(ner_model)  # load existing spaCy model
    print("Loaded model '%s'" % ner_model)
else:
    # this will create a blank english model
    ner_model = spacy.blank('en')  # create blank Language class
    print("Created blank 'en' model")



x = r"""hey guys, i got this switch up for grabs, the website is my switch patched shows that it i"""
TRAIN_DATA = [
    (x, {
        'entities': [(20, 31, 'PRODUCT'), (45, 57, 'PRODUCT')]
    })]

# add labels, Trains data based on annotations
for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

    # get names of other pipes to disable them during training
other_pipes = [pipe for pipe in ner_model.pipe_names if pipe != 'ner']
with ner_model.disable_pipes(*other_pipes):  # only train NER
    optimizer = ner_model.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in tqdm(TRAIN_DATA):
            ner_model.update(
                [text],  # batch of texts
                [annotations],  # batch of annotations
                drop=0.5,  # dropout
                sgd=optimizer,  # callable to update weights
                losses=losses)
        print(losses)