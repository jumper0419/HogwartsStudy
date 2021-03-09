#青蛙过河：
import sys
def getDiffDist(point, list):
    result = []
    for i in list:
        result.append(i - point)
    return result

while True:
    try:
        L = int(sys.stdin.readline().strip())
        l2 = sys.stdin.readline().strip().split()
        S, T, M = int(l2[0]), int(l2[1]), int(l2[2])
        l3 = sys.stdin.readline().strip().split()
        sz_list = []
        for i in l3:
            sz_list.append(int(i))

        cnt = 0
        curPoint = 0
        while curPoint <= L:
            #可能跳的point
            can_point = set(range(S+curPoint, T+curPoint+1))
            print(f"can_point: {can_point}")
            same_point = set(sz_list).intersection(can_point)
            max_point = max(same_point)
            print(same_point, '\n', max_point)
            curPoint += max_point
            cnt +=1
        print(cnt)
    except:
        break
# L = 10
# S, T, M = 2, 3, 5
# doip_list = [2,3,5,6,7]


