# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        flag = "false"
        for line in array:
            print(line)
            if target in line:
                flag = "true"
        return flag

target = 5
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
s = Solution()
print(s.Find(target, array))


# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         flag = "false"
#         for line in array:
#             if target in line:
#                 flag = "true"
#         return flag
# while True:
#     try:
#         s = Solution()
#         L = list(eval(raw_input()))
#         array = L[1]
#         target = L[0]
#         print(s.Find(target, array))
#     except:
#         break