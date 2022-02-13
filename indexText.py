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

#check similarity with entered string
print("""confess now!""")
confession = input()
for _ in range(0,len(uq1)):
    try:
        similarity1.append(model.similarity(confession, uq1[_]))
    except:
        similarity1.append(0)

print(similarity1)
print(len(similarity1))

closestWord1 = np.amax(similarity1)
index = similarity1.index(closestWord1)

print(f"your word: {confession}, closest word: {uq1[index]}, how close: {similarity1[index]}")