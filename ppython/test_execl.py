list1 = list("abcdefghijklmnopqrstuvwxyz")
# print(list1)
# a = "ab"
# len1 = len(a)
# mowei_value = a[-1]
# # print(len1, mowei_value)
# # print(list1.index(mowei_value))
# b = 26 * (len1 - 1) + int(list1.index(mowei_value)+1)
# print(b)
a = 53
# print(2*'a')
shang = a // 26
yu = a % 26
print(shang, yu)
if shang < 1 and yu != 0:
    b = list1[yu-1]
elif shang >=1 and yu != 0:
    b = list1[shang-1] + list1[yu-1]
elif shang < 1 and yu == 0:
    b = ""
elif shang == 1 and yu == 0:
    b = 'z'
else:
    b = list1[shang-2] + 'z'
print(b)
