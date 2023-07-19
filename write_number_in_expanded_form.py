def expanded_form(num):
    numbers = list(str(num))[::-1]
    result = []
    for v in range(len(numbers)):
        if numbers[v] != "0":
            result.append(numbers[v] + v * "0")

    return " + ".join(v for v in result[::-1])


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
