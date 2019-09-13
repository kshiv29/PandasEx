# List comprehension
lst = [(x, x ** 2) for x in range(2, 20) if x % 2 == 0]

for i in lst:
    print(i, end=" \n")

odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)

noprimes = [j for i in range(2, 8) for j in range(i * 2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(noprimes)

import math

print(2)
for num in range(3, 101, 2):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        print(num)

# A list of list for multiplication table
a = 5
table1 = [[a, b, a * b] for b in range(1, 11)]

print("\nMultiplication Table")
for i in table1:
    print(i)
