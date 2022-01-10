import json

data = '{"var1":"Lovish", "var2":60}'
print(data)
# print(data['var1'])                       # syntax error

parsed = json.loads(data)                   # data is parsed
print(parsed['var1'])
print(type(parsed))

data1 = {
    "channel_name":"star_worls",
    "cars":["ferrari", "bmw", "audi"],
    "fridge":("milk", "butter", 50)
}

jscomp = json.dumps(data1)
print(jscomp)