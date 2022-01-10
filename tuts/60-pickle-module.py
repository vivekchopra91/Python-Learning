import pickle

# pickling a python object  - convert text to a binary file
# cars = ["Audi", "BMW", "Merscedes", "Bentley", "Porsche"]
# file = "mycar.pkl"
# fileobj = open(file, "wb")      # binary file
# pickle.dump(cars, fileobj)
# fileobj.close()

# de-pickle an object       - read a binary file in text format
file = "mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
fileobj.close()