# Assigning string to a variable
a = "This is a string"
print(a)

i = 0
if "s" in a:
    i = i + 1

print(i)
l2 = []
# Declaring a list
l1 = [1, "a", "string", 1 + 2]
l2 = l2 + l1
print(l1)
l1.append("shiv")
print(l1)
l1.clear()
print("--------------------")
print(l2)

l2.append("sh")

print(l2)

l2.pop()
print(l2)
