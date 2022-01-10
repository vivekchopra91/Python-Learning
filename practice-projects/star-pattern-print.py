def star_pattern():
    print("*******Welcome to Star-Pattern Game*******")
    
    while True:
        try:
            num1 = int(input("Enter the number of rows you want to print : "))
            var1 = int(input("Enter 0 or 1 : "))

            if var1 == True:
                print("Below is your required star pattern :")
                for i in range(num1):
                    print((i+1) * "*")
            elif var1 == False:
                print("Below is your required star pattern :")
                for i in reversed(range(num1)):
                    print((i+1) * "*")
        
        except Exception as e:
            print("Enter a valid Number and Boolean value.")
            print("Try again.")

star_pattern()