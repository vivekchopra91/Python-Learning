
s = set([1,2,3,4])
print(s)
print(type(s))

s1 = set()
s1.add(1)
s1.add(1)       # only unique elements can be added in a set
s1.add(2)
print(s1)
s2 = s1.union({1,2,3})
print(s1, s2)

s2 = s1.intersection({1,2,3})
print(s1, s2)

print(len(s1))
print(min(s1))
print(max(s2))