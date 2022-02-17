import gensim
from gensim import models
from gensim.models import Word2Vec
import numpy as np
import csv

def csvToList(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        newList = list(reader)
    for _ in range(0,len(newList)):
        newList[_][1] = int(newList[_][1])
    return newList

def getSimilarity(confession, comparison):
    similarity = []
    for j in range(0,len(comparison)):
        similarity.append([])
        for i in range(0,len(confession)):
            similarity[j].append(0)
            try:
                similarity[j][i] = (model.similarity(confession[i], comparison[j][0]))*pow(comparison[j][1],.5)
            except:
                pass
    print(comparison)
    print(similarity)
    return similarity

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True) #without *norm_only* param

uq1 = csvToList('/Users/ethanhwang/Documents/hellDante/UQcircle1.csv')

similarity1 = []

print("""confess now!""")
confession = input()
confessionList = confession.split()
similarity1 = getSimilarity(confessionList, uq1)

closestSimilarity1 = np.argmax(similarity1, axis=0)
print(closestSimilarity1)

for _ in range(0,len(confessionList)):
    print(f"your word: {confessionList[_]}, closest word: {uq1[closestSimilarity1[_]]}, how close: {similarity1[closestSimilarity1[_]][_]}")