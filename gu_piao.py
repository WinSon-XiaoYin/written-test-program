# def money(n):
#     base = 1
#     flag = 1
#     raiseNum = 1
   
#     num = 1
#     for _ in xrange(2, n+1):
#         print base
#     	if flag == 1:
#             base += 1
#             num -= 1
#             if num <= 0:
#             	flag = 0
#                 raiseNum += 1
#         else:
#             base -= 1
#             flag = 1
#             num = raiseNum
#     return base

# mon = money(10)
# print mon

while True:
    n = int(raw_input("Please input a num: "))
    base = 1
    flag = 1
    raiseNum = 1
   
    num = 1
    for _ in xrange(2, n+1):
    	if flag == 1:
            base += 1
            num -= 1
            if num <= 0:
            	flag = 0
                raiseNum += 1
        else:
            base -= 1
            flag = 1
            num = raiseNum
    print base


