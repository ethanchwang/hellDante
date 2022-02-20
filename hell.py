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
    return similarity

def sim(listOfList):
    output = []
    for _ in listOfList:
        output.append(getSimilarity(confessionList, _))
    return output

def finalScore(listOfList):
    finalScore = []
    closestSimilarityIndex = []
    closestSimilarityNum = []
    for _ in listOfList:
        # closestSimilarity.append([])
        maxIndex = np.argmax(_, axis=0)
        closestSimilarityIndex.append(maxIndex)
        maxNums = np.amax(_, axis=0)
        closestSimilarityNum.append(maxNums)
    for _ in closestSimilarityNum:
        finalScore.append(sum(_))
    # print(f'closestSimilarity: {closestSimilarityIndex}')
    print(f'closestSimilarity: {closestSimilarityNum}')
    print(f'finalScore: {finalScore}')
    return (np.argmax(finalScore)+1)

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True) #without *norm_only* param

directory = '/Users/ethanhwang/Documents/hellDante/textWiki/'

uq1 = csvToList(f'{directory}UQCircle1.csv')
uq2 = csvToList(f'{directory}UQCircle2.csv')
uq3 = csvToList(f'{directory}UQCircle3.csv')
uq4 = csvToList(f'{directory}UQCircle4.csv')
uq5 = csvToList(f'{directory}UQCircle5.csv')
uq6 = csvToList(f'{directory}UQCircle6.csv')
uq7 = csvToList(f'{directory}UQCircle7.csv')
uq8 = csvToList(f'{directory}UQCircle8.csv')
uq9 = csvToList(f'{directory}UQCircle9.csv')

circles = [uq1, uq2, uq3, uq4, uq5, uq6, uq7, uq8, uq9]

while "matthew":
    print("""confess now!""")
    confession = input()
    confessionList = confession.split()

    c = finalScore(sim(circles))

    print(f"You have been banished to circle {c} of hell!")