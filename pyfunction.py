# functions

def add(a, b):
    sum = a + b
    return sum


result = add(3, 5)
print(result)


def defaultfunc(a, b=4, c=5):
    return a + b + c


print(defaultfunc(3))

print("-----------------------")


def f(a):
    def g(b):
        def h(c):
            return a * b * c
        return h
    return g


print(f(4)(5)(2))


print("------------factorial---------------------------")
# recursive function

def factorial(n):
    if n==1:
        return 1
    else:
        print(n)
        return n*factorial(n-1)


def sum(n):
    if n==1:
        return  1
    else:
        return n+sum(n-1)




print(factorial(5))
print(sum(5))

# lambda function

f= lambda x,y :x+y
print("lambda sum function")
print(f(2,3))

f=lambda a:lambda b:lambda c:a+b+c

print(f(1)(2)(3))