print("""Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide""")


def add(a, b):
    print(a + b)


def subtract(a, b):
    print(a - b)


def multiply(a, b):
    print(a * b)


def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print(e)


op = int(input("Please select operation from 1/2/3/4 : "))
print("-------")
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("---Result---------------")

if op == 1:
    add(a, b)
elif op == 2:
    subtract(a, b)
elif op == 3:
    multiply(a, b)
elif op == 4:
    division(a, b)
else:
    print("you enter value outta 1-4")
