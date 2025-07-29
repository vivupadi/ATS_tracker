import re

import fitz
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


import streamlit as st

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


def preprocess(text):
    text = text.lower()#lowercase
    text = re.sub(rf"[{re.escape(string.punctuation)}]", "", text)#unwanted charcters
    tokens = word_tokenize(text)#tokenize
    stop_words = set(stopwords.words("english"))
    return [token for token in tokens if token not in stop_words]    #remove stopwords

#JD
def jaccard_similarity(list1, list2):
    set_1, set_2 = set(list1), set(list2)
    intersection = set_1.intersection(set_2)
    union = set_1.union(set_2)
    return len(intersection) / len(union)


#TF-IDF
def tf_idf(text_1, text_2):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text_1, text_2])
    return cosine_similarity(tfidf[0:1],tfidf[1:2])[0][0]

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

##Main
st.title("ATS Tracker")


resume = extract_pdf('Vivek_Padayattil_Resume.pdf')

resume = clean_pdf_text(resume)

resume = preprocess(resume)

jd_text = st.text_area('Job_description', height = 300)
#breakpoint()
if jd_text:
    #job_description = clean_pdf_text(jd_text)
    job_description = preprocess(jd_text)
    breakpoint()
    #scores
    jaccard = jaccard_similarity(resume, job_description)
    breakpoint()
    cosine = tf_idf(resume, job_description)

    # Results
    print("\n--- ATS Match Results ---")
    print(f"🔹 Jaccard Similarity Score: {jaccard:.2f}")
    print(f"🔹 TF-IDF Cosine Similarity Score: {cosine:.2f}")
    print(f"🔹 Overlapping Keywords: {set(resume).intersection(set(job_description))}")
else:
    st.write('Please enter the Job description first')



