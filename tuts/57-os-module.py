import os
# print(dir(os))                                    # prints all methods and functions which can be performed by os-module

# print(os.getcwd())                                  # shows current working directory
# os.chdir("/home/vivek/python-final/tuts")           # change the current working directory (perform fucntions in that desired directory)
# print(os.getcwd())
# f = open("learning.txt")
# print(os.listdir())                                 # all files present in a directory
# os.mkdir("this")                                    # create a directory
# os.mak edirs("this/that")                            # create a directory and sub directories
# os.rename("learning.txt", "details.txt")            # change name of a file
# print(os.environ.get("HOME"))
# print(os.path.join("/home/vivek", "learning.txt"))    # join path of a file
print(os.path.exists("/home/vivek/"))                   # check of path exists or not
print(os.path.isfile("/home/vivek/"))                   # check if file exists or not
print(os.path.isdir("/home/vivek/"))                    # check if directory exists or not    