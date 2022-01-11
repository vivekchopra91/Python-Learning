# F- string
import math
import datetime
import time

g = datetime.datetime.now()
print(g)
a = 1
b = "Star"
str1 = "This is %s %s"%(a, b)       # one way of formatting a string
print(str1) 

# time.sleep(5)                     # sleep function to hold the program for 5 sec before the next part is executed
c = "This is {0} {1}"               # 2nd method
d = c.format(a , b)
print(d)

# time.sleep(5)
e = f"This is {a} {b}." 
f = f"The value of Sin(60) is {math.sin(60)}."
print(e)                            # 3rd menthod - f-string
print(f)
h = datetime.datetime.now()
print(h)

x = time.process_time()             # gives total process time the fucntion took to perform
print(x)