# A simple Python function to check
# whether x is even or odd
def evenOrOdd(x):
    if (x % 2 == 0):
        print('{} is even'.format(x))
    else:
        print('{} is odd'.format(x))


print("-------------------------")
evenOrOdd(11)


def swap(x, y):
    x, y = y, x


a = 12
b = 13
a, b = b, a

swap(a, b)
print(a, b)
