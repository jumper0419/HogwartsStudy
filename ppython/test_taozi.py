from math import ceil

a = "3 11 6 7 8"
list1 = a[:-2].split(" ")
# print(list1)
list2 = []
for x in list1:
    list2.append(int(x))
hours = int(a[-1])
# print(list1, hours)
min1 = min(list2)
max1 = max(list2)
# print(min1, max1)
for gg_ele in range(min1, max1+1):
    hour_sum = 0
    # print(f"gg_ele: {gg_ele}")
    for v in list2:
        hour_sum += ceil(v / gg_ele)
        # print(hour_sum)
    if hour_sum <= 8:
        print(gg_ele)
        # print(hour_sum)
        break
