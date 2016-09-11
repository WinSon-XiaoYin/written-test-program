# -*- coding: utf-8 -*-
import math

"""
腾讯笔试题：输入一个数，找出所有两个质数之和等于这个数的质数对。
"""

Num = int(raw_input())

numList = [2, 3, 5, 7]

allNum = [num for num in xrange(8, 1000)]

for num in allNum:
  for i in range(8, num):
    if num % i == 0 or num % 3 == 0 or num % 2 == 0 or num % 5 == 0 or num % 7 == 0:
        break
    else:
      numList.append(num)
      break

"""
def gen_num():
    for num in xrange(2, 1000):
        for i in xrange(2, num):
            if num == 2 or num == 3 or num ==5 or num == 7:
                yield num
            elif num % i == 0 or num % 3 == 0 or num % 2 == 0 or num % 5 == 0 or num % 7 == 0:
                break
            else:
                yield num
                break

gen = gen_num()
numDict = {}
index = 0
for value1 in gen:
    for value2 in gen:
        if value1 + value2 == Num:
            numDict[value1] = value2

"""
numDict = {}
for index, value1 in enumerate(numList):
  for value2 in numList[index:]:
    if value1 + value2 == Num:
      numDict[value1] = value2

for num in numDict:
    print num, numDict[num]
