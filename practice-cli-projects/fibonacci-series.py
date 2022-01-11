# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .....
# Using Iterative Method


def fibonacci(n):
    if n < 0:
        print("Please enter a positive integer.")
    else:
        i1 , i2 = 0 , 1
        for i in range (n):
            print(i1, end=" ")
            i = (i1) + (i2)
            i1 = i2
            i2 = i
            i +=1 

a = int(input("How many terms do you wish to print? : "))
print(f"The fibonacci series for {a} numbers is : ")
fibonacci(a)
print("\n")