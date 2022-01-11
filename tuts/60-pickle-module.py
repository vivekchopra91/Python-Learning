import pickle

# pickling a python object  - convert text to a binary file
# cars = ["Audi", "BMW", "Merscedes", "Bentley", "Porsche"]
# cars2 = {"Audi":"R8", "BMW":"Z4", "Merscedes":"S-class", "Porsche":"Cayene"}
# file = "mycar.pkl"
# fileobj = open(file, "wb")      # binary file
# pickle.dump(cars, fileobj)
# fileobj = open(file, "ab")        # append to a pickle file
# pickle.dump(cars2, fileobj)
# fileobj.close()

# de-pickle an object       - read a binary file in text format
file = "mycar.pkl"
fileobj = open(file, "rb")
# mycar = pickle.load(fileobj)
# mycar2 = pickle.load(fileobj)
# print(mycar)
# print(mycar2)
# print(type(mycar))
# print(type(mycar2))

while True:
    try:
        # print(fileobj.tell())
        print(pickle.load(fileobj))
    except Exception as e:
        # print("End of file !!")
        break

fileobj.close()

# to update an object in the middle of a pickle file, the whole file needs to be updated or else the file can get curropt
