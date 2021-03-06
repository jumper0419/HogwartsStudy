# while True:
#     try:
# a = input()
a = "1234567890abcd9.+12345.678.9ed"
list1 = []
for v in list(a):

maxLen, maxStrs, curLen, curStr = 0, [], 0, ""
# print(list(enumerate(a)))
list1 = list(enumerate(a))
# print(list1[0], list1[0][0])
for i, v in enumerate(a):
    if v == "." and i == 0 or i == len(a)-1:
        continue
    elif v == "+" or v == "-" and i == len(a)-1:
        continue
    elif v == "+" or v == "-" and list1[i+1][1].isnumeric():
        maxLen, maxStrs, curLen, curStr = 0, [], 1, f"{v}"
        if curLen > maxLen:
            maxLen = curLen
            maxStrs = [curStr]
        elif curLen == maxLen:
            maxStrs.append(curStr)
        print(f"2: {maxStrs}")
    elif v == "." and list1[i-1][1].isnumeric() and list1[i+1][1].isnumeric():
        curLen += 1
        curStr += v
        if curLen > maxLen:
            maxLen = curLen
            maxStrs = [curStr]
        elif curLen == maxLen:
            maxStrs.append(curStr)
        print(f"3: {maxStrs}")
    elif v.isnumeric():
        curLen += 1
        curStr += v
        if curLen > maxLen:
            maxLen = curLen
            maxStrs = [curStr]
        elif curLen == maxLen:
            maxStrs.append(curStr)
        print(f"4: {maxStrs}")
    else:
        curLen = 0
        curStr = ""
# print(maxStrs)
# print("".join(maxStrs) + "," + str(maxLen))
    # except:
    #     break
