#用进制的思想
# def getChars(length):
#     return [getChar(index) for index in range(length)]
#
# def getChar(number):
#     factor, moder = divmod(number, 26) # 26 字母个数
#     modChar = chr(moder + 65)          # 65 -> 'A'
#     if factor != 0:
#         modChar = getChar(factor-1) + modChar # factor - 1 : 商为有效值时起始数为 1 而余数是 0
#     return modChar

import sys
# print(ord('a')) # 97


def getChars(num):
    #解决27进位的问题
    factor, moder = divmod(num-1, 26)
    modChar = chr(moder + 97)
    if factor > 0:
        modChar = getChars(factor) + modChar
    return modChar

#方法一：
if __name__ == "__main__":
    while True:
        try:
            a = int(sys.stdin.readline().strip())
            print(getChars(a))
        except:
            break

#方法二
# while True:
#     try:
#         a = int(sys.stdin.readline().strip())
#         list1 = list("abcdefghijklmnopqrstuvwxyz")
#         jz_list = []
#         result = ""
#         while a:
#             yu = (a-1) % 26
#             a = (a-1) // 26
#             jz_list.insert(0, yu)
#         print(jz_list)
#         for i in jz_list:
#             result += list1[i]
#         print(result)
#     except:
#         break
