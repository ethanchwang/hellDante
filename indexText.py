#initialize gensim stuff
import gensim
from gensim import models
from gensim.models import Word2Vec
import numpy as np

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True) #without *norm_only* param

def txtToList(path):
    file = open(path).read()
    return file.split()

def csvToList(path):
    my_file = open(path, "r")
    my_file.close()
    return print(my_file.read().split("\n"))

def removeNonChar(list):
    newlist = []
    for _ in range(0,len(list)):
        newlist.append(''.join(filter(str.isalpha, list)))
    return newlist

def lowerCase(list):
    newlist = []
    for _ in range(0,len(list)):
        newlist.append(list[_].lower())
    return newlist

def removeDup(list):
    uq = []
    for _ in list:
        if _ in uq :
            pass
            # print(f"duplicate: {_}!")
        else:
            # print(f"new element: {_}!")
            uq.append(_)
    return uq

#convert text to list
circle1List = txtToList('/Users/ethanhwang/Documents/hellDante/circle1.txt')

#remove duplicates and save to uq1
uq1 = removeDup(circle1List)

#make uq1 lowercase
uq1 = lowerCase(uq1)

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
print(closestSimilarity1[0])
print(closestSimilarity1[1])
print(closestSimilarity1[2])

for _ in range(0,len(confessionList)):
    print(f"your word: {confessionList[_]}, closest word: {uq1[closestSimilarity1[_]]}, how close: {similarity1[closestSimilarity1[_]][_]}")