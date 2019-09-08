# # Exception handling
#
# #print(6/0)
#
# # file not found
# # r=open("file",'r')
#
#
#
# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)
#
#
# try:
#     n=int(input("Enter an Integer : "))
# except ValueError :
#     print("This is Not an integer")
#
# # multiple exception and finally block
#
# try:
#     sum=0
#     file=open("numbers.txt",'r')
#     for number in file:
#         sum=sum+1.0/int(number)
#     print(sum)
# except ZeroDivisionError:
#     print("number in the file is equal 0 !")
# except IOError:
#     print("File don't exist")
# finally:
#     print(sum)
#     file.close()
#
#
#
# def RaiseException(a):
#     if type(a) !=type('a'):
#         raise ValueError("This is Not a string")
#
# a=1
#
# try:
#     RaiseException(a)
# except ValueError as e:
#     print(e)
#  raise and assert keyword


def TestCase(a,b) :
     assert a<b,"a is greater than b"
try:
    TestCase(10,11)
except AssertionError as e:
    print(e)

