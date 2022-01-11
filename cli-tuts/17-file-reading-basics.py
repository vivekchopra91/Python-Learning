'''
"r" - open file in read mode / read a given file - default mode
"w" - open file in write mode / over-write a given file
"x" - creates new file if it does not exits
"a" - open file in append mode / add information to a given file
"t" - open file in text mode - default mode
"b" - open file in binary mode
"+" - open file in read and write mode.
'''

f = open("learning.txt", "rt")       # r - default mode
content = f.read()
print(1, content)
content = f.read()
print(2, content)       # blank, as a complete file can be read only once
f.close()       # always close a file after performing an operation.


f = open("learning.txt")
content = f.read(5)     # read first 5 letters of the file
print(content)
content = f.read(5)     # read next 5 letters
print(content)
f.close()

f = open("learning.txt")
content = f.read()
for line in content:
    print(line, end="")
f.close()

f = open("learning.txt")
content = f.readline()      # reads 1st line of the file
content = f.readline()      # reads 2nd line
content = f.readline()      # reads 3rd line
print(content)
f.close()

f = open("learning.txt")
print(f.readlines())        # output in form of list
f.close()
