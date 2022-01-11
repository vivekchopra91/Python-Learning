
def matrix (m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o

def multiple(a, b) :
    result = []
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    
    for r in result:
        print(r)

m = int(input("Enter the value of 'm'\n"))
n = int(input("Enter the value of 'n'\n"))

print("Enter matrix A")
A = matrix(m, n)
print(A)

print("Enter matrix B")
B = matrix(m,n)
print(B)

C = multiple(A,B)


# alternate method :-->
# import numpy as np

# def matrix (m, n):
#     o = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             inp = int(input(f"Enter O[{i}][{j}]"))
#             row.append(inp)
#         o.append(row)
#     return o

# def multiple(x, y):
#     result= []
#     result = np.dot(x, y)
#     print("The multiple of above 2 matrices is : ")
#     for r in result:
#         print(r)

# m = int(input("Enter the value of 'm'\n"))
# n = int(input("Enter the value of 'n'\n"))

# print("Enter matrix A")
# A = matrix(m, n)
# print(A)

# print("Enter matrix B")
# B = matrix(m,n)
# print(B)

# C = multiple(A, B)