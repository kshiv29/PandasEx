# data structure

tup = (1, 'abc', 2, 'cde')

tup2 = 3, 'efg', 13

tup3 = "A",

print(tup)
print(tup2)
print(tup3)

try:
    tup[3] = 5
except Exception as e:
    print(e)

# Python program to illustrate list

# creates a empty list
nums = []

# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")

print(nums)
