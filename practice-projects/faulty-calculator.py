while True:
    print("Please choose the operation to perform : (*, +, -, /, %, **)")
    o = input()
    n1 = int(input("Enter 1st number : "))
    n2 = int(input("Enter 2nd number : "))
    if n1 == 45 and n2 == 3 and o =="*":
        print("The product of above 2 numbers is : 555")
    elif n1 == 56 and n2 == 9 and o =="+":
        print("The sum of above 2 numbers is : 77")
    elif n1 == 56 and n2 == 6 and o =="/":
        print("The quotient of above 2 numbers is : 4")
    elif o == "+":
        print(f"The sum of above 2 numbers is : {n1 + n2}")
    elif o == "-":
        print(f"The difference of above 2 numbers is : {n1 - n2}")
    elif o == "*":
        print(f"The product of above 2 numbers is : {n1 * n2}")
    elif o == "/":
        print(f"The quotient of above 2 numbers is : {n1 / n2}")
    elif o == "**":
        print(f"The solution is : {n1 ** n2}")
    elif o == "%":
        print(f"The remainder of above 2 numbers is : {n1 % n2}")
    else:
        print("Invalid input, please try again.")

    if((input("Do you want to continue calculating? If yes type 'Y' else type 'N' \n")).capitalize() =='Y'):
        continue
    else:
        print("Thank You for using the Calculator")
        break