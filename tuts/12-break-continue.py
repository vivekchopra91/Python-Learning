# i = 0
# while True:
#     if i < 5:
#         i+=1
#         continue
#     print(i+1, end=" ")
#     if(i == 44):
#         break
#     i+=1


while True:
    inp = int(input("Enter a number : "))
    if inp >100:
        print("Congrats! You have entered a number greater than 100.")
        break
    else:
        print("Try again!\n")
        continue
    