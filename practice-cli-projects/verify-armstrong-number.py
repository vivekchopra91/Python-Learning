a = int(input("Enter a number : "))
b = str(a)
d = len(str(a))
sum = 0

for c in b:
    sum = sum + ((int(c))**d)
# print(sum)

if sum == a:
    print(f"{a} is an armstrong number.")
else:
    print(f"{a} is NOT an armstrong number.")
