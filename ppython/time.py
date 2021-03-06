import time
# 西方时间格式： Fri Mar  5 10:31:08 2021
from sqlalchemy import null

print(time.asctime())
# 以秒计时： 1614911468.0950065
print(time.time())
# 以元祖格式返回： time.struct_time(tm_year=2021, tm_mon=3, tm_mday=5,
#                                tm_hour=10, tm_min=31, tm_sec=8,
#                                tm_wday=4, tm_yday=64, tm_isdst=0)
print(time.localtime())
# 以想要格式返回: 2021-03-05 10:33:40
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 2天前
now = time.time()
format_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
print(f"现在的时间： {format_now}")
two_day = now - 24*60*60*2
format_two_day = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(two_day))
print(f"2天前：{format_two_day}")

a = "sssss"
d = [a]
print(d)
print(enumerate(a))
for i,v in enumerate(a):
    print(f"i: {i}, v: {v}")

d = [1, 2, 3, 4]
print(d[::-1])
# print(d.index(5))
# if str(d.index(5)) == "":
#     print("not exist")
a = ["20-year", "-stu-dent"]
print(a[1].find("-"))