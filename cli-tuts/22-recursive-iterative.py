# def func1(str1):
#     func1(str1)             # this will throw a recursion error
#     return "This is a string : " + str1
# print(func1("Welcome to my python tutorial."))


# n! = n * n-1 * n-2 * n-3 ....... * 1      # factorial of n natural numbers
# n! = n * (n-1!)                           # another way of writing a factorial of n numbers

# iterative approach
def factorial_iter(n):
    a = 1
    for i in range (n):
        a = a * (i+1)
    return a

num1 = int(input("Enter a number : "))
print(f"The factorial of {num1} using Iterative Method is :", factorial_iter(num1))



# recursive approach
def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recur(n-1)

num2 = int(input("Enter a number : "))
print(f"The factorial of {num2} using Recursive Method is :", factorial_recur(num2))