class Employee:
    
    def  __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def func1(self):
        return f"The Employee is {self.fname} {self.lname}"

    @property                               # to run below function without calling it as a function
    def print_email(self):
        return f"{self.fname}.{self.lname}@example.com"

    @print_email.setter
    def print_email(self, string):
        print("Setting Now...")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @print_email.deleter
    def print_email(self):
        self.fname = None
        self.lname = None

lovish = Employee("Lovish", "Puri")
print(lovish.print_email.lower())

print(type(lovish))
print(id(lovish))
print(type(lovish.print_email))

a = "This is a string"
print(dir(a))           # all the functions that can be performed on the variable/string
print(dir(lovish))

import inspect
print(inspect.getmembers(lovish))