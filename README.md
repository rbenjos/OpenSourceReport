# OpenSourceReport
hosting the files used for the final report of the course.
this minimal project identifies drugs in free text, prints them, and highlights them in an HTML file.

![Alt Text](https://media.giphy.com/media/QZXgXcl0S825c5s8lF/giphy.gif)

## the files in the repository:

### ECR_example.txt
an electronic record for example.

### drug_labeling.py
the code used for labaleing the drugs, printing them, 
and tagging them on the HTML file, all using the med7 model.

### drug_labeling_example.html
the HTML file with the drugs identified and tagged.

## project setup:

clone this repository and run the following commands in the terminal:

`pip install -U pip setuptools wheel`

`pip install spacy`

after that, run drug_labeling.py.
