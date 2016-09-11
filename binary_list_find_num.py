# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        for i in array:
          if type(i).__name__ == "int":
            if i == target:
              return True
          else:
            return self.Find(i, target)
        return False
            
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
sol = Solution()
if sol.Find(array, 14):
    print "ok"
else:
    print "bad"

