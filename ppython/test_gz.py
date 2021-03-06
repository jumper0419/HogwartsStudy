input = "a11b2bac3bad3abcd2"
ala = ""
num = ""
result = {}
list1 = list(enumerate(input))
for i, v in enumerate(input):
    # print(i, v)
    if i != len(list1)-1:
        add_value = list1[i+1][1]
        if v.isdigit() and add_value.isalpha():
            if ala != "":
                result[ala] = num
            ala = ""
            num = ""
        elif v.isalpha():
            ala += v
        elif v.isdigit():
            num += v
    else:
        result[ala] = num


print(result)
