# -*- coding: utf-8 -*-

from math import sqrt

"""
求一个数的平方根序列和
"""

class Solution:
    # @param firstNum, a int num
    # @param num, a int num
    def sqrtSum(self, firstNum, num):
	answer = firstNum
        for _ in xrange(num-1):
	    pinFanGen = sqrt(firstNum)
	    answer += pinFanGen
	    firstNum = pinFanGen
	print "%.2f" % answer
        
while True:
	sol = Solution()
	inputStr = raw_input()
	numList = inputStr.split()

	firstNum = int(numList[0])
	num = int(numList[1])
    
	sol.sqrtSum(firstNum, num)
    
