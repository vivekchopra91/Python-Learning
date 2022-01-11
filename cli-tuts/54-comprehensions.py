# l1 = []
# for i in range(1, 100):
#     if i%3 == 0:
#         l1.append(i)

# list comprehensions
l1 = [i for i in range(1, 50) if i%3==0]
print(l1)

# dictionary comprehensions
d1 = {i:f"item {i}" for i in range(1,50) if i%5==0}
print(d1)
d2 = {value:key for key,value in d1.items()}            # reverse a dictionart values
print(d2)

# set comprehensions
s1 = {i for i in range(1, 50) if i%4==0}
print(s1)
print(type(s1))

# generator comprehensions
g1 = (i for i in range(1, 50) if i%2==0)
print(type(g1))
print(g1)
for items in g1:
    print(items, end=" ")
print()


# practice projects
print("What kind of comprehension do you wish to generate ? :")
c = int(input("""
    1. List
    2. Dictionary
    3. Set
    4. Generator
    """))
no_of_list = int(input("How many items do you wish to add : "))
input_string = input("Enter the element separated by space ")
list1 = input_string.split(" ")
if no_of_list == len(input_string.split(" ")):
    if c==1:
        ls = [i for i in list1]
        print(type(ls))
        print(ls)
    elif c==2:
        dict1 = {i:f'item - {i}' for i in list1}
        print(type(dict1))
        print(dict1)
    elif c==3:
        s ={i for i in list1}
        print(type(s))
        print(s)
    elif c == 4:
        g = (i for i in list1)
        print(type(g))
        print(g)
    else:
        print("invalid input.")    
else:
    print("The values do not match the desired count, please try again.")