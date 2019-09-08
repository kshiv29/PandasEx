# Python3 program to get input from user

# accepting integer from the user
# num1 = int(input("Enter num1 : "))
# num2 = int(input("Enter num2 : "))
#
# result = num1* num2
#
# print("multiplication of the two is {0}".format(result))

print("number is", "abc", 20)


# function
def hello(a):
    print("Hello {0}".format(a))
    print("Hello Again !!!!!")


hello("shiv")

hello("vinay")

# Python program to illustrate
# function with main
# def getInteger():
#     result = int(input("Enter integer: "))
#     return result
#
#
# def Main():
#     print("Started")
#     # calling the getInteger function and
#     # storing its returned value in the output variable
#     output = getInteger()
#     print(output)
#
#
# # now we are required to tell Python
# # for 'Main' function existence
# if __name__ == "__main__":
#     Main()

# Python program to illustrate
# math module
import math


def Main():
    num = float(input("Enter any decimal Number : "))
    val = math.fabs(num)
    print(val)

if __name__ == "__main__":
    Main()
