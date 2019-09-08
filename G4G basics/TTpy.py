# # . Find The Most Frequent Value In A List.
# test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
# print(test.count(4))
# print(max(set(test), key = test.count))


# Check The Memory Usage Of An Object.
# import sys
# x = 'a'
# print(sys.getsizeof(x))

# Checking if two words are anagrams

from collections import Counter


def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


print(is_anagram('geek', 'eegk'))

print(is_anagram('geek', 'peek'))
