def hcf_calculate(x, y):
    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return f"The HCF of above 2 number is {hcf}"


if __name__ == "__main__":
    a = int(input("Enter 1st number :"))
    b = int(input("Enter 2nd number :"))
    c = hcf_calculate(a, b)
    print(c)