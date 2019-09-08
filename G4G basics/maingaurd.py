# source -- https://stackoverflow.com/questions/419163/what-does-if-name-main-do

# When the Python interpeter reads a source file, it first defines a few special variables. In this case, we care about the __name__ variable.

# When Your Module Is the Main Program
#
# If you are running your module (the source file) as the main program, e.g. maingaurd.py
# print("before import")
# import math
#
# print("before functionA")
# def functionA():
#     print("Function A")
#
# print("before functionB")
# def functionB():
#     print("Function B {}".format(math.sqrt(100)))
#
# print("before __name__ guard")
# if __name__ == '__main__':
#     functionA()
#     functionB()
# print("after __name__ guard")
#
#
# def functionA():
#     print("a1")
#     from maingaurd import functionB
#     print("a2")
#     functionB()
#     print("a3")
#
# def functionB():
#     print("b")
#
# print("t1")
# if __name__ == "__main__":
#     print("m1")
#     functionA()
#     print("m2")
# print("t2")
#
# # output --
# t1
# m1
# a1
# t1
# t2
# a2
# b
# a3
# m2
# t2

def functionA():
    print("a1")
    from maingaurd import functionB
    print("a2")
    functionB()
    print("a3")


def functionB():
    print("b")


print("t1")
print("m1")
functionA()
print("m2")
print("t2")
