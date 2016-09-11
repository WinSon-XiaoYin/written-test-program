"""
美团笔试题：求红包总金额，要求只能隔一个以上取红包，而且第一个和最后一个不能同时取
"""
N = int(raw_input())
  
L = [[0]*N for i in range(N)]


for i in xrange(N):
  redPackage = raw_input()
  redPackage = redPackage.split(',')
  redPackageList = []
  for package in redPackage:
    redPackageList.append(package)
  L[i] = redPackageList
  
flag = 0
for subList in L:
  lineSum = 0 
  for index, value in enumerate(subList[0::2]):
    if value < subList[index+1]:
        value = subList[index+1] 
        flag += 1
    if flag != 0:
        index += flag
    if index == len(subList)-1:
      break
    lineSum += int(value)
  print lineSum
