def  count(str):
    dict = {}
    for v in list(str):
        if v not in dict.keys():
            dict[v] = str.count(v)
    # print(dict)
    return dict

t = "x.nowcoder.com"
s = "oooy"
t_dict = count(t)
s_dict = count(s)
set_s = set(s_dict.keys())
set_t = set(t_dict.keys())
flag = True
# print(set_s.intersection(set_t))
if set_s.intersection(set_t) == set_s:
    for i in set_s:
        if s_dict[i] != t_dict[i]:
            flag = False
else:
    flag = False
if flag:
    print("Yes")
else:
    print("No")






