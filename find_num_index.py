# -*- coding: utf-8 -*-

"""
用二分法查找一个升序列表中是否存在该数，如果不存在则输出-1-应该存在的位置，存在则返回它所在的位置。
"""

num = int(raw_input())
count = int(raw_input())
inputStr = raw_input()
inputStr = inputStr.split()
inputList = []
for i in xrange(count):
    inputList.append(int(inputStr[i]))

def binaryFind(num, lists):
    start = 0
    end = len(lists) - 1
    found = False
    index = 0
    while start <= end and not found:
        midPoint = (start + end) // 2
        if lists[midPoint] == num:
            found = True
            index = lists.index(num)
            return index
        else:
            if num < lists[midPoint]:
                index  = midPoint
                print "<index", index
                end = midPoint - 1
            else:
                index = midPoint + 1
                print ">index", index
                start = midPoint + 1
    return -1-index

answer = binaryFind(num, inputList)
print answer
