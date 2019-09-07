# File management
import os
print(os.curdir)

path="C:\\Users\\shiv8.kumar\\Desktop"

os.chdir(path)

file= open("write.txt","w+")
file .write("hello ! this is the fisr line of the file")
print(file.tell())
file.seek(0)
print(file.read())

file.close()