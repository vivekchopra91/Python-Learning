"""
Iterable -->  __iter()  or __getitem__()
Iterator -->  __next__()
Iteration --> 
"""
def gen(n):
    for i in range(n):
        yield i
g = gen(999999999999999999)
# print(g)                                    # <generator object gen at 0x7efc83e8dc80>
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# for i in g:
#     print(i)
# a = "lovish"
# print(iter(a))          # generate iter object


# Practice Projects
# This is for calculating factorial of n numbers using genarotors:-
    # using if/else statements - to get factorial number at nth position
def factcal(n):
    if n==1:
        return 1
    return n*factcal(n-1)
    # using while loop - to generate factorial series upto nth number
def factgen(n):
    i=1
    while i<=n:
        yield factcal(i)
        i += 1
num = int(input("Enter your number to calculate factorial of?\n"))
g = factcal(num)
print(f"The factorial of {num} is at object{factgen(num)}.")
print(f"The factorail of {num} is {g}.")
# for i in g:   # to generate entire seres
#     print(i, end=" ")
    
# This is for generating fibonacci series of n numbers using genarotors:-
    # using if/else statements - get fibonacci number on nth iteration
def fibocal(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibocal(n-1) + fibocal(n-2)
    # using while loop - generate series.
def fibogen(n):
    i = 1
    while i<=n:
        yield fibocal(i)
        i += 1
num = int(input("Enter your number to get fibonacci series?\n"))
g = fibogen(num)
print(f"Below is the fibonacci series of first {num} numbers.")
for i in g:
    print(i, end=" ")
print()