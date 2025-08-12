#Intermediate
#import transformers
from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity

#Cosine similarity with embeddings

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_score(list1, list2):
    text_1 = " ".join(list1)
    text_2 = " ".join(list2)
    embedding = embedding_model.encode([text_1, text_2])
    return cosine_similarity([embedding[0]], [embedding[1]])[0][0]