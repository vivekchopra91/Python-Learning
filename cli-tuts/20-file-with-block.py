with open ("learning2.txt") as f:
    a = f.read(10)
    b = f.readlines()
    print(a)
    print(b)


try:
    c = f.readlines()           # this will throw error
    print(c)
except Exception as e:
    print(e)