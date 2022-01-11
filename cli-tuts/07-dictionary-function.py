d1 = {"Hritik":"Roshan", "Varun":"Dhawan", 
    "Alia":"Bhatt", "Tamanna":"Bhatia", 
    "Kapoor":{"Shradha", "Ranbir", "Bebo", "Lolo"}}

print(type(d1))
print(d1["Hritik"])
print(d1["Kapoor"])
d1["Siddharth"] = "Malhotra"    # add new items
print(d1)
del d1["Varun"]                 # remove an item
print(d1)

# d2 = d1.copy()      # make new dictionary, so any change in d2 will not effect d1
d2 = d1                # any change in d2 will also be updated in d1
print(d2)
d2["Deepika"] = "Padukone"
print(d2)
print(d1)       

del d2["Hritik"]
print(d2)
print(d1)

d2.update({"Priyanka" : "Chopra"})
print(d2)
print(d1)

print(d1.keys())    # prints all keys
print(d1.items())   # prints key-value pairs
print(d1.values())  # prints all values