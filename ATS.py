import preprocess
import Basic_ats
import Intermediate
from preprocess import *
from Basic_ats import *
from Intermediate import *

import streamlit as st


##Main
st.title("ATS Tracker")


resume = preprocess(clean_pdf_text(extract_pdf('Vivek_Padayattil_Resume.pdf')))


jd_text = st.text_area('Job_description', placeholder='Enter the job description', height = 350)
#breakpoint()
if jd_text:
    job_description = preprocess(clean_pdf_text(jd_text))

    #scores
    jaccard = jaccard_similarity(resume, job_description)
    cosine = tf_idf(resume, job_description)
    semantic = semantic_score(resume, job_description)

    # Results
    st.write(" ATS Match Results")
    st.write(f"🔹 Jaccard Similarity Score: {jaccard:.2f}")
    st.write(f"🔹 TF-IDF Cosine Similarity Score: {cosine:.2f}")
    st.write(f"🔹 Semantic Similarity Score: {semantic :.2f}")
    st.write(f"🔹 Overlapping Keywords: {set(resume).intersection(set(job_description))}")
    st.write(f"🔹 Missing Keywords: {(set(job_description)) - set(resume)}")
else:
    st.write('Please enter the Job description first')



