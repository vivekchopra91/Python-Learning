a = 10          # global variable, can be used multiple times inside the file

def func1(n):
    # a = 5       # local variable, only applicable inside the function
    b = 15
    global a        # permission to change the value of global variable a inside the function
    a = a +10
    print(a,b)
    print(n, "I have printed a line.")

func1("This is func1.")
print(a)
# print(b)        # this will throw an error, since b is a local variable



# 2nd example
def func2():
    x = 30
    def func3():
        global x            # this will search for a global variable outside the function, but there is none
        x = 50              # value will not change to 50 for local variable
    print("pre-func3()", x)
    func3()
    print("post-func3()", x)

func2()
print(x)            # 50 will be assigned as global variable outside the function