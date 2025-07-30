import re

import fitz
import string

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


#Extract pdf
def extract_pdf(path):
    docs = fitz.open(path)
    all_text = ""
    for doc in docs:
        blocks = doc.get_text("blocks")

        #sor by y(top-to-botoom), then x(left-to-right)
        blocks =sorted(blocks, key = lambda b: (round(b[1]), round(b[0])))

        doc_text = "\n".join(block[4] for block in blocks if block[4].strip())
        all_text += doc_text + "\n"

    return all_text

def clean_pdf_text(text):
    text = re.sub(r"-\n", "", text)       # fix hyphenated line breaks
    text = re.sub(r"\n+", "\n", text)     # normalize line breaks
    text = re.sub(r"\s{2,}", " ", text)   # collapse double spaces
    return text.strip()

def preprocess(text):
    text = text.lower()#lowercase
    text = re.sub(rf"[{re.escape(string.punctuation)}]", "", text)#unwanted charcters
    tokens = word_tokenize(text)#tokenize
    stop_words = set(stopwords.words("english"))
    return [token for token in tokens if token not in stop_words]    #remove stopwords