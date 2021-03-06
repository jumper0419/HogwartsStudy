from functools import reduce

squ = [x**2 for x in range(10)]
print(squ)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
a = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(a)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 多维数组 转换行列
matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
         ]
res = [[row[i] for row in matrix] for i in range(4)]
"""
for i in range(4):
    for row in matrix:
        return row[i]
"""
print(res)

sqr = lambda n: n ** 2
print(sqr(2))

# map(func, [list]) #list 中的每个元素作为func的参数传入，输出
l1 = map(sqr, range(3))
print(l1)  # 输出迭代器的地址 <map object at 0x000001563A2ED8B0>
print(list(l1))  # 输出结果 [0, 1, 4]

add = lambda x,y: x * y
# reduce(func, [list]) 累加，将第一次运算的结果作为第二次的输入
l1 = reduce(add, [1, 2, 4, 6])
print(l1) #48
"""
reduce运算过程：
第一次：a = add(1,2) -> 2
第二次：a = add(a,4) -> 8
第三次：a = add(a,6) -> 48
"""

#filter: 符合留下，不符合去除【判断1~1000的回文数】
def is_huiwen(n):
    l1 = list(str(n))
    l2 = l1[::-1]
    if l1 == l2:
        return True
    return False
result = filter(is_huiwen, range(1,1001))
print(list(result))



