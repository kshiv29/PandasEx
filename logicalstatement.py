g="Abcdefgh"
h="Abcdefg"
a=12
b=25
print((g>h) and not(a>=b))
print(((g>h) and not(a>=b))and 1)
passerby="hello"

if passerby=="hello" or passerby=="Hi":
    print("Hello! How are You")

if True:
    print("testing  if statement")
#if else elif
name="Shiv"
if name=="Shiv":
    print("Hello Shiv , how are you")
elif name=="Sanaya":
    print("Hello Sanaya , how are you")

passerby_speech="Hip"
if passerby_speech=="Hello":
    print("Hi")
elif passerby_speech=="Hi":
    print("Hello")
else:
    print("Hey !")

#ternary operator
a=13
a=7 if 3**2>9 else 24
print(a)

#for loop and range , for loop need a iterating sequence (list,tuple,dict,set,string)
fruits=["apple","banana","orange"]
for i in fruits:
    print(i)

for i in range(1,10,2):
    print(i)

string2="apple"
for char in string2:
    print(char)

print("-------------------")
# 3 x 3 matrix
for i in range(1,4):
    for j in range(1,4):
            print('{:>2}|'.format(i*j), end=" ")

    print("")

# 10 x 10 multiplication  table

# for i in range(1, 11):
#     print('{:<3}|'.format(i), end="")
#     for j in range(1, 11):
#         print('{:>4}'.format(i*j), end="")
#
#     if i==1:
#         print('\n{:#^44}'.format(""), end="")
#
#     print("")


# while loop
condition=10

while condition!=0:
    print(condition)
    condition=condition-1


print("i am here ")
# break and continue statements
i=0
list1=[1,2,3,4,5]
while list1[i]<=4:
    print(list1[i])
    i=i+1
    if i>2:
        break

for ij in range(1,6):
    if ij==4:
        continue
    print(ij*2)

