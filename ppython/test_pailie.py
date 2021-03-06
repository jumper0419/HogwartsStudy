import itertools
#排列 ：(1,2)和(2,1)是不同的
mylist = list(itertools.permutations([1,2,3,4], 2))
print(mylist)
print(len(mylist))

#组合： (1,2)和(2,1)是相同的
mylist = list(itertools.combinations([1,2,3,4,5], 2))
print(mylist)
print(len(mylist))

#笛卡尔积
#repeat 重复3次
mylist = list(itertools.product("QWERTYUIOP", repeat=3))
print(mylist)
print(len(mylist))
