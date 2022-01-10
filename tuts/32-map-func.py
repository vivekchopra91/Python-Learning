
num1 = ["10", "20", "30", "40", "50"]
# for i in range(len(num1)):
#     num1[i] = int(num1[i])
num1 = list(map(int, num1))
print(num1)
num2 = num1[2] + 1
print(num2)


def sq(a):
    return a*a
def cube(a):
    return a*a*a

l1 = [20,31,52,28,9,15,25,16]
# l2 = list(map(sq, l1))
l2 = list(map(lambda x : x*x, l1))
print(l2)

func1 = [sq, cube]
for i in (l1):
    val = list(map(lambda x : x(i), func1))
    print(val)
