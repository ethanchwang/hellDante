import csv

def txtToList(path):
    file = open(path).read()
    return file.split()

def listToCSV(list, path):
    nestedList = []
    for _ in range(0,len(list)):
        nestedList.append([])
        nestedList[_].append(list[_].lower())
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

#remove all noncharacters
uq1 = removeNonChar(uq1)

listToCSV(uq1,'/Users/ethanhwang/Documents/hellDante/uq1.csv')