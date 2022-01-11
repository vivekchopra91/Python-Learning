# Variables : containers of values
var1 = "Hello World!"       # var1 is a string type variable
var2 = 4                    # var2 is a integer type variable
var3 = 32.5                 # var3 is a float type variable
var4 = "This is Vivek."
var5 = "55"
var6 = "44"

print(var1)
print(type(var1))           # <class 'str'>
print(type(var2))           # <class 'int'>
print(type(var3))           # <class 'float'>
print(type(var5))           # <class 'str'>

print( var1 + var4 )        # str can be added only to str
print( var2 + var3 )        # int/float can be added to either of them


# Typecasting
print(int(var5) + int(var6))
print(10 * var1)            # string concatination
print(10 * str(int(var5) + int(var6)))
print(10 * "Hello World!\n")