def func1():
    print("This is function 1.")

func2 = func1

func2()

def func3(num):
    if num == 0:
        return print
    elif num == 1:
        return sum

a = func3(0)
print(a)

def decorator1(func1):
    def execnow():
        print("Executing now...")
        func1()
        print("Executed.")
    return execnow

def what_is_python():
    print("Python is a programming language.")

what_is_python = decorator1(what_is_python)
what_is_python()