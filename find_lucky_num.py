# -*- coding: utf-8 -*-

count = int(raw_input())

dijige = count
a = ['0', '1', '2', '3', '5', '6', '8', '9']
numList = []

if count <= 2**2-2:
    c = 1
elif 2**2-2 < count <= 2**3-2:
    c = 2
elif 2**3-2 < count <= 2**4-2:
    c = 3
elif 2**4-2 < count <= 2**5-2:
    c = 4
elif 2**5-2 < count <= 2**6-2:
    c = 5
elif 2**6-2 < count <= 2**7-2:
    c = 6
elif 2**7-2 < count <= 2**8-2:
    c = 7

def makeNumList(c):
    for i in range(4, 10**c):
        yield i

num = makeNumList(c)
for value in num:
        j = str(value)
        for x in j:
            if x not in a:
                numList.append(value)
                break
while len(numList) != 2**(c+1)-2:
    for index, value in enumerate(numList):
        j = str(value)
        for x in j:
            if x in a:
                try:
                    del numList[index]
                    break
                except:
                    numList = numList
"""
count = count**2
def makeAList(count, numList):
    for _ in range(count):
        for index, value in enumerate(numList):
            j = str(value)
            for x in j:
                if x in a:
                    try:
                        del numList[index]
                        break
                    except:
                        numList = numList
                        return numList
    return numList

numList = makeAList(count, numList)
"""

print numList[dijige-1]
