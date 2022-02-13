#initialize gensim stuff
import gensim
from gensim import models
from gensim.models import Word2Vec
import numpy as np

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True) #without *norm_only* param

#index
circle1 = open('/Users/ethanhwang/Documents/hellDante/circle1.txt').read()

def convert(x):
    return (x.split())

circle1List = convert(circle1)
#print(circle1List)

uq1 = []

#remove duplicates and save to uq1
for _ in circle1List:
    if _ in uq1 :
        print(f"duplicate: {_}!")
    else:
        print(f"new element: {_}!")
        uq1.append(_)

#make uq1 lowercase
for _ in range(0,len(uq1)):
    uq1[_] = uq1[_].lower()

similarity1 = []

print("""confess now!""")
confession = input()
confessionList = convert(confession)
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
print(closestSimilarity1[0])
print(closestSimilarity1[1])
print(closestSimilarity1[2])

for _ in range(0,len(confessionList)):
    print(f"your word: {confessionList[_]}, closest word: {uq1[closestSimilarity1[_]]}, how close: {similarity1[closestSimilarity1[_]][_]}")