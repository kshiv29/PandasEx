String="This is the string"
String1="this is 1 string"
print(String)
# print(len(String))
# print(String[::-1])
# print(String*2)
# print("hello" " guys")
# word="Ford"
# word= "L"+word[1:]
# print(word)

formatstarting= "Today I will Learn {0} hours  {1}".format(2,"python")
formatstarting2 ="Today I will Learn {x} hours  {y}".format(x=3,y="python")

print(formatstarting2)
print('{:<20}'.format("shiv kumar yadav"))
print('{:>20}'.format("shiv kumar yadav"))
print('{:o}'.format(10))
print('{:b}'.format(10)) #for binary
print('I\'m a "python learner"')
print(r'this is path C:\number\nan') #raw string
print("""\
        Hello:
        
            user Defined Look
                hallo ihr seid junge
""")