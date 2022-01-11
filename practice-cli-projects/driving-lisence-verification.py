name = input("Enter your name : ")
age = int(input("Enter your age : "))

if age == 18:
    print(f"Hello {name}, please visit the DMV authoroties to get your physical documents verification & further process.")
elif age > 18:
    print(f"Hello {name}, you are eligible to get a driver's lisence. kindly visit to DMV for test.")
else:
    print(f"Hello {name}, you are not yet eligible to get a driver's lisence. kindly re-visit after {18-age} year.")