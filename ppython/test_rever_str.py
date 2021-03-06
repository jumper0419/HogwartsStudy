a = "I am an 20-years 20 out--standing @ * -stu-dent"
# print(list)
list2 = a.split()
result = []
for value in list2:
    # print(value)
    if value.isalnum():
        result.append(value)
        # print("aaaa", result)
    elif value.find("--") > -1:
        tmp = value.split("--")
        for item in tmp:
            result.append(item)
        # print("ccc", result)
    elif value.find("-") > -1:
        if list(value)[0] == "-":
            result.append("".join(list(value)[1:]))
        elif list(value)[len(value)-1] == "-":
            result.append("".join(list(value)[:len(value)-1]))
        else:
            result.append(value)
        # print("bbbb", result)
print(" ".join(result[::-1]))

