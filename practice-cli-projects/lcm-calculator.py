
def lcm(a , b):
    if a > b:
        max = a
    else:
        max = b
    while True:
        if (max%a == 0 and max%b == 0):
            break
        max +=1
    print(f"{max} is the LCM of the above 2 numbers.")
            

if __name__ == "__main__":
    a = int(input("Enter 1st number :"))
    b = int(input("Enter 2nd number :"))
    c = lcm(a, b)
    # print(c)