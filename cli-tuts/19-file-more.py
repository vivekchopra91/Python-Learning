f = open("learning2.txt")
print(f.tell())             # shares where the pointer is in the file.
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(10)                  # moves pointer at the required input point.
print(f.readline())
f.seek(40)
print(f.readline())
print(f.tell())
f.close()