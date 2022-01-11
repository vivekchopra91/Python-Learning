var1 = int(input("Enter 1st number : "))
var2 = int(input("Enter 2nd number : "))
var3 = int(input("Enter 3rd number : "))

# if var3>var2:
#     if var3>var1:
#         print(f"{var3} is the greatrest number added.")
#     else:
#         print(f"{var1} is the greatrest number added.")
# else:
#     if var2>var1:
#         print(f"{var2} is the greatrest number added.")
#     else:
#         print(f"{var1} is the greatrest number added.")

if var3>var2 and var3>var1:
    print(f"{var3} is the greatrest number added.")
elif var2>var3 and var2>var1:
    print(f"{var2} is the greatrest number added.")
elif var3 == var2 == var1:
    print("All 3 numbers added are equall")
else:
    print(f"{var1} is the greatrest number added.")

