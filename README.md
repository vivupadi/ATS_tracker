# 📄ATS Score & Keyword Suggestions
A compute instance application that helps job seekers improve their resumes by tracking ATS (Applicant Tracking System) scores based on the provided job description and providing personalized CV improvement suggestions.
The app stores and displays your CV suggestion,needing to change only the job description.

<img width="862" height="735" alt="image" src="https://github.com/user-attachments/assets/5d38b5c6-19d5-4d70-862a-d5d2f1d01543" />


## The Algorithm  

The algorithm behind uses basic NLP keyword matching and advanced LLM-based embedding matching.

🚀 [Live Demo](https://example.com) — Also featured on my Portfolio Website.  

---  
## ✨Features  
**ATS Similarity Score Calculation** – Upload your resume and compares the similarity with the job description and suggest missing keywords.

**CV Suggestions History** – View all previous suggestions to track your improvements.

**User-Friendly Interface** – Minimal, clean, and mobile-responsive.

**Deployed on Azure AKS** – Scalable and cloud-ready deployment.

## 🛠️Tech Stack  
-**Frontend**: Streamlit (Python)

-**Backend**: Python

-**Deployment**: Azure Kubernetes Service (AKS) + Azure Container Registry (ACR) or Azure Container Instance

-**Containerization**: Docker

-**Version Control**: Git & GitHub

## 📖Installation on Local System
**Clone the repository**

git clone https://github.com/vivupadi/ATS_tracker.git

cd ATS_tracker/app

**Create virtual environment**

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install dependencies**

pip install -r requirements.txt

**Run the Application**

streamlit run app.py


## 🚀 Deployment Workflow for Cloud

**Architecture Overview**

┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Azure ACR     │    │   Azure AKS      │    │   Application   │
│                 │    │                  │    │                 │
│ Container       │──▶│ Kubernetes       │───▶│ Streamlit App   │
│ Registry        │    │ Orchestration    │    │ Multi-Language  │
│                 │    │                  │    │ NLP Processing  │
└─────────────────┘    └──────────────────┘    └─────────────────┘


**Build Image on ACR (no local build needed)**

az acr build --registry <ACR_NAME> --image ats-app:v1 .


**Deploy to AKS**

kubectl apply -f deployment.yaml


**Check Pods & Service**

kubectl get pods
kubectl get svc


**Access Application**
Open the EXTERNAL-IP in browser:

http://<EXTERNAL-IP>


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
