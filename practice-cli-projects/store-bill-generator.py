# Grocery store bill & receipt generator
sum = 0
a = dict()
while True:
    userInput = input("Press (i) to input values to bill & (q) to generate the receipt : ")
    if userInput == "i":
        item = input("Enter an item : ")
        qty = int(input("Enter its quantity : "))
        price = int(input("Enter price/item : (Rs.) "))
        sum = sum + (price*qty)
        a[item] = [qty, price]
        print("")
    elif userInput == "q":
        print("")
        print("7-Eleven -> Bill Summary :")
        print("***********")
        print ("{:<10} {:<9} {:<10}".format('Item', 'Qty', 'Price/pc'))
        for k, v in a.items():
            Item = k
            Qty, Price = v
            print ("{:<10} {:<10} {:<8}".format(Item, Qty, Price))
        print(f"Grand total : Rs. {sum}.")
        print("***********")
        print("Thank you for your visit to our store.")
        print("Please visit again.")
        print("***********")
        break