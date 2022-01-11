import pickle as pk
import requests

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
print(data)

# to create a pickle file
# l1 = data.split("\n")
# print(l1)

# l2 = [item.split(",") for item in l1 if len(item)!=0]
l2 = [item.split(",") for item in data.split("\n") if len(item)!=0]
print(l2)

with open("myiris.pkl", "wb") as f:
    pk.dump(l2, f)


# to read the above created pickle file
# with open("myiris.pkl", "rb") as f:
#     print(pk.load(f))