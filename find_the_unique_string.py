def find_uniq(arr):
    for word in set(arr):
        for letter in set(word):
            if sum([1 if letter in w else 0 for w in arr]) == 1:
                return word
            else:
                continue


res = ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']
print(find_uniq(res))
