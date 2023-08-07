def duplicate_count(text):
    text = text.lower()
    letters = [x for x in text]
    return len(set([x for x in letters if letters.count(x) > 1]))


print(duplicate_count("abcde"))
<<<<<<< HEAD
print(duplicate_count("aabbcde"))
<<<<<<< HEAD
=======
#print(duplicate_count("aabbcde"))
>>>>>>> 982fbc7 (comment test 7)
#print(duplicate_count("aabBcde"))
#print(duplicate_count("indivisibility"))
#print(duplicate_count("Indivisibilities"))
#print(duplicate_count("aA11"))
=======
print(duplicate_count("aabBcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
>>>>>>> 057cfc4 (comment test 1)
#print(duplicate_count("ABBA"))
