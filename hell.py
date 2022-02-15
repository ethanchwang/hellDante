import gensim
from gensim import models
from gensim.models import Word2Vec
import numpy as np

def csvToList(path):
    my_file = open(path, "r")
    newList = my_file.read().split("\n")
    my_file.close()
    return newList

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True) #without *norm_only* param

print(model.similarity('eagle', 'python'))
# print(model.most_similar(positive=['unbaptized']))

uq1 = csvToList('/Users/ethanhwang/Documents/hellDante/uq1.csv')

similarity1 = []

print("""confess now!""")
confession = input()
confessionList = confession.split()
for j in range(0,len(uq1)):
    similarity1.append([])
    for i in range(0,len(confessionList)):
        similarity1[j].append(0)
        try:
            similarity1[j][i] = model.similarity(confessionList[i], uq1[j])
        except:
            pass

print(similarity1)
print(len(similarity1))

closestSimilarity1 = np.argmax(similarity1, axis=0)
print(closestSimilarity1)

for _ in range(0,len(confessionList)):
    print(f"your word: {confessionList[_]}, closest word: {uq1[closestSimilarity1[_]]}, how close: {similarity1[closestSimilarity1[_]][_]}")