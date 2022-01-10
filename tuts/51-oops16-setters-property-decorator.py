class Employee:

    def  __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@example.com"

    def func1(self):
        return f"The Employee is {self.fname} {self.lname}"

    @property                               # to run below function without calling it as a function
    def print_email(self):
        if self.fname or self.lname == None:
            return "Email is not set, please set it using setter."
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
rahul = Employee("Rahul", "Sharma")

print(lovish.func1(), "and his email is :", lovish.print_email.lower())

rahul.fname = "Rohit"
print(rahul.print_email.lower())

lovish.print_email = "atul.kohli@example.com"
print(lovish.fname)
print(lovish.lname)
print(lovish.print_email)

del lovish.print_email