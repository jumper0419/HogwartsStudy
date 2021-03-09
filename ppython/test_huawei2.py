import sys

if __name__ == "__main__":
    L = int(sys.stdin.readline().strip())
    l2 = sys.stdin.readline().strip().split()
    S, T, M = int(l2[0]), int(l2[1]), int(l2[2])
    doip_list1 = sys.stdin.readline().strip().split()
    doip_list = []
    for doip in doip_list1:
        doip_list.append(int(doip))
    # print(l2, doip_list)
    # print(L, S, T, M)
    pass_len = 0
    pass_doip_list = [0]
    # print(S, T)
    while pass_len < L:
        #     len = lambda x: x for x in range(S, T+1)
        # for len in range(S, T + 1):
        len = T
            # print(len)
        pass_len += len
        pass_doip_list.append(pass_len)
    set_pass = set(pass_doip_list)
    set_dopi = set(doip_list)
    # print(set_pass)
    # print(set_dopi)
    jj_list = set_pass.intersection(set_dopi)
    # print(jj_list)
    print(jj_list.__len__())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     for v in values:
    #         ans += v
    # print(ans)
    #
    # L = 10
    # S, T, M = 2, 3, 5
    # doip_list = [2, 3, 5, 6, 7]
    # # print(type(doip_list))
    # # dopi_list = doip.split(" ")
    # # print(dopi_list)
    # pass_len = 0
    # pass_doip_list = [0]
    # # print(S, T)
    # while pass_len < L:
    #     #     len = lambda x: x for x in range(S, T+1)
    #     for len in range(S, T + 1):
    #         # print(len)
    #         pass_len += len
    #         pass_doip_list.append(pass_len)
    # set_pass = set(pass_doip_list)
    # set_dopi = set(doip_list)
    # # print(set_pass)
    # # print(set_dopi)
    # jj_list = set_pass.intersection(set_dopi)
    # print(jj_list)
    # print(jj_list.__len__())