# one liner functions / lambda functions / anonymous functions

plus = lambda x,y : x+y
minus = lambda a,b : a-b

print(plus(10,5))
print(minus(10,5))



# 2nd example
def a_first(a):
    return a[1]

l1 = [[10,12], [3,4], [50,16], [15,16]]
# l1.sort(key = a_first)
l1.sort(key = lambda x:x[1])
print(l1)