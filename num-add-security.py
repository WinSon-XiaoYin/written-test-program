"""
数字加密
"""

inputStr = raw_input()
inputList = list(inputStr)

lists = []
count = 1
for index,value in enumerate(inputList):
    if lists:
        if lists[-2] != value:
            lists.append(value)
            for i in inputList[index+1:]:
                if i == value:
                    count += 1
                    if index+1 == len(inputList)-1:
                        lists.append(str(count))
                        count = 1
                        break
                else:
                    lists.append(str(count))
                    count = 1
                    break
        else:
            continue
    else:
        lists.append(value)
        for i in inputList[index+1:]:
            if i == value:
                count += 1
            else:
                lists.append(str(count))
                count = 1 
                break

answer = "".join(lists)
print answer

