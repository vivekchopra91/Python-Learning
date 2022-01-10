# *args & **kwargs

# def func1(a, b, c, d, e):         # write all arguments manually in a function
#     print(a, b, c ,d, e)

def func1(normal_argument, *args, **kwargs):
    # print(args[0])
    print("Now a normal argument will get printed")
    print(normal_argument)
    
    print("\nNow *args will get printed")
    for item in args:
        print(item)
    
    print("\nNow **kwargs will get printed")
    for key, value in kwargs.items():
        print(key, value)

str1 = "This is a normal argument, in form of a string."
l1 = ["Python", "Django", "Pygame", "Numpy", "Java"]
dict1 = {"Python":"1st subject", "Data Engineering":"2nd subject", "Power BI":"3rd subject"}
func1(str1, *l1, ** dict1)

