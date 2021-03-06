
def get_sheng_money(list, current_money):
    hua_money = 0
    if line[2] > line[1]:
        extra_money = 1 * (line[2] - line[1])
    else:
        extra_money = 0

    if list[0] >= 100:
        # <=15天：5元；>15天：3元
        if line[1] > 15:
            hua_money = extra_money + 5 * 15 + 3 * (line[1] - 15)
        else:
            hua_money = extra_money + 5 * line[1]
    elif line[0] >= 50：
        # <=15天：3元； >15天：1元
        if line[1] > 15:
            hua_money = extra_money + 3 * 15 + 1 * (line[1] - 15)
        else:
            hua_money = extra_money + 3 * line[1]
    else:
        # 每天1元
        hua_money = extra_money + 1 * line[1]

    sheng_money = current_money - hua_money
    if sheng_money <= 0:
        return 0
    else:
        return sheng_money

def main():
    a = [[120, 10, 10], [80, 10, 3], [30, 10, 12]]
    total_money = 300
    sheng_money = 300

    for line in a:
        print(line)
        while sheng_money >= line[0]:
            get_sheng_money(line, sheng_money)

if __name__ == "__main__":
    main()
