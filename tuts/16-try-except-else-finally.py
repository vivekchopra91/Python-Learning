num1 = (input("Enter 1st number : "))
num2 = (input("Enter 2nd number : "))

try:
    print("the sum of above 2 number is : ", int(num2)+int(num1))
except Exception as e:
    print(e)
# except ValueError as e:
#     print(e)

print("This is an important information.")



# using else and finally

f1 = open("learning2.txt")

try:
    # f2 = open("learning.txt")
    f2 = open("1.txt")
except Exception as e:
    print(e)
else:
    print("This will run only if try/except is not running.")
finally:
    print("Run this in any case, even if try/except is running :")
    f1.close()
    # f2.close()
    print("Files closed.")

print("Important function.")