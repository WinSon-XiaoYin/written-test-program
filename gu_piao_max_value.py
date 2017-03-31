# -*- coding: utf-8 -*-

"""
每日股票跌涨序列，每日只能买入和卖出一次，求最大利润。
"""

inputStr = raw_input()
inputStr = inputStr.split(',')
inputList = []
for i in inputStr:
    inputList.append(int(i))

maxList = []
for index, value in enumerate(inputList[::-1]):
    for i in inputList[:len(inputList)-index]:
        maxList.append(value-i)

maxNum = max(maxList)
print maxNum
