# few of the functions are described below

l1 = ["Burger", "Pizza", "Paratha", "Maggie", "Bhatura", "Rajma-Chawal", 56, 7, 89]
l2 = [4,3,22,50,1,6]

print(l1)
print(l1[0])
print(len(l1))      # length of the list(items count)
print(sum(l2))      # sum of all the numbers in the list
l2.sort()
print(l2)           # [1, 3, 4, 6, 22, 50]
l2.reverse()
print(l2)           # [50, 22, 6, 4, 3, 1]

print(l2[1:])       # print all elements afte 1st index elements
print(l2[::])
print(l2[::2])      # skip 1 element
print(l2[::3])      # skip 2 elements
print(max(l2))
print(min(l2))

l2.append(100)      # add 100 at the end of the list
print(l2)
l2.insert(2, 50)    # add 50 @ 2nd index of the list
print(l2)
l2.remove(50)       # removes 1st 50 which appears on the list
print(l2)
l2.pop()            # removes last element from the list
print(l2)
l2[3] = 98          # change value @ 3rd index of the list
print(l2)

# List is Mutable       -    value can be changed if/when required
# tuple is immutable    -    cannot change its value once set
tp = (1,2,5)
print(tp)

# reverse numbers/variable value
a = 2
b = 7
a,b = b,a
print(a,b)