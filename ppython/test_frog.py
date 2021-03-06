L = 10
S, T, M = 2, 3, 5
doip_list = [2,3,5,6,7]
# print(type(doip_list))
# dopi_list = doip.split(" ")
# print(dopi_list)
pass_len = 0
pass_doip_list = [0]
# print(S, T)
while pass_len < L:
#     len = lambda x: x for x in range(S, T+1)
    for len in range(S, T+1):
        # print(len)
        pass_len += len
        pass_doip_list.append(pass_len)
set_pass = set(pass_doip_list)
set_dopi = set(doip_list)
# print(set_pass)
# print(set_dopi)
jj_list = set_pass.intersection(set_dopi)
print(jj_list)
print(jj_list.__len__())


# print((lambda x: x + 1)(2))
x = [lambda x: x for x in range(10)]
print(x[0])

