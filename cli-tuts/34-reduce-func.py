from functools import reduce

l1 = [20,31,52,28,9,15,25,16]

# num = 0
# for i in l1:
#     num = num + i
# print(num)

num1 = reduce(lambda x, y: x+y, l1)
print(num1)
