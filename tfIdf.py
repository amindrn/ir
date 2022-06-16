import csv
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import numpy as np
file = open('tabnak150Page.csv', encoding="utf8")
type(file)
csvreader = csv.reader(file)
docs = []
for row in csvreader:
    docs.append(row[2])
# words = []
# for d in docs:
#     words.extend(d.split())
# vocab = np.array(words)
# vocab = np.unique(vocab)
vectorizer = TfidfVectorizer(lowercase=True)
vectorizer.fit(docs)
tfidf_docs = vectorizer.fit_transform(docs)
vectorizer.vocabulary_
docs_tfidf = vectorizer.transform(docs)
type(docs_tfidf), docs_tfidf.shape
z = docs_tfidf[0].A
def quaryPro(query):
    tfidf_query = vectorizer.transform([query])[0]
    cosines = []
    for d in tqdm(tfidf_docs):
        cosines.append(float(cosine_similarity(d, tfidf_query)))
    k = 10
    sorted_ids = np.argsort(cosines)
    for i in range(k):
        cur_id = sorted_ids[-i-1]
        print('----------------------------------------------',cosines[cur_id],'--------------------------------------------------------')
        print(docs[cur_id])
while True:
    print('###################################################وارد کنید','################################################')
    query = input()
    quaryPro(query)
    print('----------------------------------------------------------------------------------------------------------------')


