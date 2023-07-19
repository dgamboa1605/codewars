def expanded_form(num):
    num1, num2 = str(num).split(".")
    list1 = list(num1)[::-1]
    list2 = list(num2)
    result = []
    result2 = []

    for v in range(len(list1)):
        if list1[v] != "0":
            result.append(list1[v] + v * "0")

    for r in range(len(list2)):
        if list2[r] != "0":
            result2.append(list2[r] + "/1" + (r + 1) * "0")

    return " + ".join(result[::-1] + result2)


print(expanded_form(807.304))
print(expanded_form(1.24))
print(expanded_form(7.304))
print(expanded_form(0.04))
