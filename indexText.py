import csv

directory = '/Users/ethanhwang/Documents/hellDante/'
nWordsRemove = 300
c1 = 'circle1'

def csvToList(path):
    my_file = open(path, "r")
    newList = my_file.read().split("\n")
    my_file.close()
    return newList

def txtToList(path):
    file = open(path).read()
    return file.split()

def listToCSV(list, path):
    nestedList = []
    for _ in range(0,len(list)):
        nestedList.append([])
        nestedList[_].append(list[_][0].lower())
        nestedList[_].append(list[_][1])
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(nestedList)

def removeNonChar(list):
    newlist = []
    for _ in range(0,len(list)):
        newlist.append(''.join(filter(str.isalpha, list[_])))
    return newlist

def lowerCase(list):
    newlist = []
    for _ in range(0,len(list)):
        newlist.append(list[_].lower())
    return newlist

def removeDup(list):
    uq = {}
    for _ in list:
        if _ in uq:
            f = uq.get(_)
            uq.update({_ : (f+1)})
            pass
        else:
            uq[_] = 1
    return uq

def removeCommonWords(uq, n):
    commonWords = csvToList('/Users/ethanhwang/Documents/hellDante/commonWords2.csv')
    print(f'length before removing common words: {len(uq)}!')
    for _ in range(0,min(n,1000)):
        try:
            uq.pop(commonWords[_].lower())
        except:
            pass
            print(f'{commonWords[_]} not found!')
    print(f'length after removing common words: {len(uq)}!')
    print(list(uq.items()))
    return list(uq.items())

def txtToUQ(c):
    listToCSV(removeCommonWords(removeDup(removeNonChar(lowerCase(txtToList(f'{directory}{c}.txt')))),nWordsRemove),f'{directory}UQ{c}.csv')

txtToUQ(c1)