from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#JD
def jaccard_similarity(list1, list2):
    set_1, set_2 = set(list1), set(list2)
    intersection = set_1.intersection(set_2)
    union = set_1.union(set_2)
    return len(intersection) / len(union)


#TF-IDF
def tf_idf(list1, list2):
    text_1 = " ".join(list1)
    text_2 = " ".join(list2)
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text_1, text_2])
    return cosine_similarity(tfidf[0:1],tfidf[1:2])[0][0]