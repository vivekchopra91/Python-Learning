# a = input("What is your name? ")
# b = int(input("How much do you earn? "))
# if b==0:
#     raise ZeroDivisionError("b is 0, so stopping the programme")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed.")             # so that further code does not run and saves time if there is error

# print(f"Hello {a}")
# code taking 2 hour to run


c = input("Enter your name : ")
try :
    print(a)

except Exception as e:
    if c == "Sanam":
        raise ValueError("Sanam is blocked by the company.")

    print("Exception handeled.")