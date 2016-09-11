# -*- coding: utf-8 -*-

"""
输入一个0-1000的数，求这个范围内的水仙花数
"""

class Solution:
    def findFlower(self, m, n):
        answerList = []
        for i in xrange(m, n+1):
            baiWei = i/100%10
            shiWei = i/10%10
            geWei = i%10
            answer = baiWei**3 + shiWei**3 + geWei**3
            if i == answer:
                answerList.append(str(i))
        if len(answerList) == 0:
            print "no"
        else:
            answerStr = ' '.join(answerList)
            print answerStr
            
while True:
    sol = Solution()
    num = raw_input()
    numList = num.split()
    sol.findFlower(int(numList[0]), int(numList[1]))
