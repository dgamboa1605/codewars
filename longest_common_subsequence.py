def lcs(x, y):
    count = 0
    result = ""
    for i in range(len(y)):
        for g in range(count, len(x)):
            if y[i] == x[g]:
                result += y[i]
                count = g + 1
                break

    return result


print(lcs("abcdef", "abc"))
print(lcs("abcdef", "acf"))
print(lcs("anothertest", "notatest"))
print(lcs("finaltest", "zzzfinallyzzz"))
