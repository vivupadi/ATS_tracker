import preprocess
import Basic_ats
import Intermediate
from preprocess import *
from Basic_ats import *
from Intermediate import *

import streamlit as st

#Initiliaze
if "jd_text" not in st.session_state:
    st.session_state.jd_text = ""
if "jaccard" not in st.session_state:
    st.session_state.jaccard = ""
if "cosine" not in st.session_state:
    st.session_state.cosine = ""
if "semantic" not in st.session_state:
    st.session_state.semantic = ""



##Main
st.title("ATS Tracker")


@st.cache_data
def load_resume(resume_path):
    resume = preprocess(clean_pdf_text(extract_pdf(resume_path)))
    return resume

load_pdf = st.file_uploader("Upload your resume", type=['pdf'])
if load_pdf:
    resume = load_resume(load_pdf)
else:
    print("Upload Resume")
#resume = load_resume('Vivek_Padayattil_Resume.pdf')


st.session_state.jd_text = st.text_area('Job_description', value=st.session_state.jd_text, placeholder='Enter the job description', height = 350)
#jd_text = st.session_state.jd_text
#breakpoint()

def calculate_scores(jd_text):
    if jd_text:
        job_description = preprocess(clean_pdf_text(jd_text))

        #scores
        st.session_state.jaccard = jaccard_similarity(resume, job_description)
        st.session_state.cosine = tf_idf(resume, job_description)
        st.session_state.semantic = semantic_score(resume, job_description)

        # Results
        scr = st.container(border=True)
        scr.write(" ATS Match Results")
        scr.write(f"🔹 Jaccard Similarity Score: {st.session_state.jaccard:.2f}")
        scr.write(f"🔹 TF-IDF Cosine Similarity Score: {st.session_state.cosine:.2f}")
        scr.write(f"🔹 Semantic Similarity Score: {st.session_state.semantic :.2f}")
        scr.write(f"🔹 Overlapping Keywords: {set(resume).intersection(set(job_description))}")
        scr.write(f"🔹 Missing Keywords: {(set(job_description)) - set(resume)}")


def clear_jd():
    st.session_state.jd_text = ""
    st.session_state.jaccard = ""
    st.session_state.cosine = ""
    st.session_state.semantic = ""

calculate_scores(st.session_state.jd_text)


if st.button('Clear and Enter New Job Description'):
    clear_jd()






