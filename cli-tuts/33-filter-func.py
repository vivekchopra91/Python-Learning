
l1 = [20,31,52,28,9,15,25,16]
def is_greater(num):
    return num>25

a = list(filter(is_greater, l1))
print("These number are greater than 25:", a)