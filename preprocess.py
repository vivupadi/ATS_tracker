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
    def detect_lang():
        return detect_lang
    text = re.sub(rf"[{re.escape(string.punctuation)}]", "", text)#unwanted charcters
    tokens = word_tokenize(text)#tokenize
    custom_stop_words = {'spirit', 'written', 'handson', 'value', 
                         'embrace', 'inclusive',  
                         'eg', 'spoken', 'sites', 'concepts', 'tasks', 'fluency', 
                         'real', 'results', 'requirements',
                         'degree', 'supporting', 'take', 'bridge', 'client', 'implementing', 
                         'enjoy', 'practical', 'contribute', 'business', 'stem', 'mindset', 
                         'sharp', 'willingness', 'field', 'internships', 
                         'technology', 'regularly',  'excellent', 
                          'clearly', 'environment', 'get', 'us', 'also',
                         'solutions', 'travel', 'well', 'part', 'highly', 'exciting', 'receive'
                         'create', 'growth'}
    if lang == 'de':
        stop_words = set(stopwords.words("german"))
    elif lang == 'en':
        stop_words = set(stopwords.words("english"))
    stop_words = set(stopwords.words("english"))
    extended_stopwords = stop_words.union(custom_stop_words)
    return [token for token in tokens if token not in extended_stopwords]    #remove stopwords