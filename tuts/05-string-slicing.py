
# index ---------(-3)(-2)(-1)
# index 0123456789----------
str1 = "This is a new world."

# string slicing
print(str1)
print(str1[0])          # 1st letter @ index 0   
print(str1[0:4])        # letters from index 0 to 3 - 1st 4 letters
print(str1[0:40])       # letters from index 0 to 39 - 1st 40 letters which are available

print(str1[0:40:2])     # skip 1 letter and print
print(str1[0:40:3])     # skip 2 letters and print and so on
print(str1[0:])         # print complete string all the words
print(str1[:40])        # print string upto 40 letters
print(str1[::])         # print complete string all the words
print(str1[-10:-2])

# String functions
print(len(str1))        # get lenth of the string
print(type(str1))       # get type of the variable
print(str1.isalnum())   # false : since the string is not in alpha-numeric format
print(str1.isalpha())
print(str1.endswith("world."))      # check is the string ends with the word "world"
print(str1.count("i"))      # count the times "i" is in the string
print(str1.capitalize())    # capitalize 1st letter of the sentense
print(str1.find("is"))      # find if & where "is" is present in the string
print(str1.lower())         # change entire string to lower case
print(str1.upper())         # change entire string to upper case    
print(str1.replace("is", "are"))    # replace word
