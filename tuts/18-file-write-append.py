# writing to a file
# f = open("learning2.txt", "w")
# f.write("Writing a file using python.")
# f.close()

# appending to a file
# f = open("learning2.txt", "a")
# a = f.write("\nAppend a new line to the file.\n")
# print(a)    # number of characters written to a file 
# f.close()

# handle read and write both
f = open("learning2.txt", "r+")
print(f.read())
f.write("thank you\n")
print(f.read())
f.close()