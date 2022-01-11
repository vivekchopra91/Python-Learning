# ==   --> value equality   --> two objects have the same value
# is   --> reference equality   --> to references - refer to the same object

a = [1,2,3]
b = a

print(b == a)           # True
print(b is a)           # True

c = a[:]                # creating a copy

print(b == c)           # True
print(a == c)           # True
print(c is a)           # False
print(c is b)           # False


d = [4, 7, "54"]
e = [4, 7, "54"]
print(d is e)           # False
print(d == e)           # True