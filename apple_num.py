# -*- coding: utf-8 -*-

"""
网易测试开发岗，苹果分成6袋和8袋
输入要买的苹果数N，问最少的袋数买苹果N，如果不能满足，则输出-1。
"""

num = int(raw_input())
apple_list = [6, 8]

count = 0
flag = 0
for x in xrange(0, 20):
    for j in xrange(0, 20):
        if x*apple_list[0] + j*apple_list[1] == num:
            count = x + j
            print x, j
            flag = 1
            break
    if flag == 1:
        break
		
if flag == 0:
    count = -1
print count
