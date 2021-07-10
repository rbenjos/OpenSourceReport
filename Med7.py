import sys
import spacy
import re
from spacy.lang.en import English

DRUG_COLOR = "#e89ff0"
DRUG_LABEL = 5792857178182177913

# Downloading the model we will use for tagging
med7 = spacy.load("en_core_med7_lg")


col_dict = {}

# Setting up the colors for the labels
for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = DRUG_COLOR
options = {'ents': ['DRUG'], 'colors': col_dict}


# Loading the text we will analyze
file = open(sys.argv[1])
text = file.read()
doc = med7(text)

# Printing the drugs we identified
drugs = [entity for entity in doc.ents if entity.label == DRUG_LABEL]
for drug in set(drugs):
    print(drug)

# Labeling them ON the text in an HTML file
html = spacy.displacy.render(doc, style="ent", page=True, options=options)
new_address = sys.argv[1][:-3] + 'med7.html'
new_file = open(new_address, 'w')
new_file.write(html)

