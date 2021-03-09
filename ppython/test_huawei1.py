# 可以参考test_execl2.py
import sys
while True:
    try:
        a = int(sys.stdin.readline().strip())
        list1 = list("abcdefghijklmnopqrstuvwxyz")
        jz_list = []
        result = ""
        while a:
            yu = (a-1) % 26
            a = (a-1) // 26
            jz_list.insert(0, yu)
        # print(jz_list)
        for i in jz_list:
            result += list1[i]
        print(result)
    except:
        break