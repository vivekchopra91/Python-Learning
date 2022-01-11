def print1(str1):
    return(f"{str1} is a string function.")

def add1(a,b):
    return(a+b+6)

print("And the name is : ", __name__)
# code written after this, can only be run inside this file , it cannot be imported to another file
if __name__ =="__main__":
    print(print1("hello,"))
    print(add1(5,5))