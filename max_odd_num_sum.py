# -*- coding: utf-8 -*-

"""
这是网易测试开发岗的第二道编程题，
输入一个数N，求1-N之间所有数的最大奇约数之和。
结果是对的，但是测试的时候提示超时了。
"""

nums = int(raw_input())

# def gen(nums): 
#     for num in xrange(1, nums+1):
#         if num % 2 != 0:
#             print num,
#             yield num
#         else:
#             for x in xrange(num//2, 0, -1):
#                 if x % 2 != 0 and num % x == 0:
#                     print x,
#                     yield x
#                     break
# g = gen(nums)
# answer = reduce(lambda x, y: x+y, g)
# print answer

# num_list = []
# for num in xrange(1, nums+1):
#         if num % 2 != 0:
#         	num_list.append(num)
#         else:
#             for x in xrange(num//2, 0, -1):
#                 if x % 2 != 0 and num % x == 0:
#                     num_list.append(x)
#                     break
# answer = reduce(lambda x, y: x+y, num_list)
# print answer

count = 0
for num in xrange(1, nums+1):
        if num % 2 != 0:
        	count += num
        else:
            for x in xrange(num//2, 0, -1):
                if x % 2 != 0 and num % x == 0:
                    count += x
                    break
print count
