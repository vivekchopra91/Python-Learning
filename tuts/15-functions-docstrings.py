a = 9
b = 8
c = sum((a, b))     # built in function
print(c)

def func1():
    print("Hello you are in user defined function.")
func1()

def func2(a, b):
    return (f"the sum of the given 2 number is : {a+b}")
d=func2(5,10)
print(d)

def func3(a , b):
    """This is a function, which will return average of 2 numbers."""      # this is a doc-string, 1st line written in a function is called a doc-string
    average = (a+b)/2
    return(f"the average of the given numbers is : {average}")
e = func3(20, 30)
print(e)
print(func3.__doc__)        # see doc-string to get information on the function.