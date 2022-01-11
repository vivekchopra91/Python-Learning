# Public - Accesable to all public/anyone who wants to use it
# Private - Accessable to only a selected few
# Protected - Accessable to only self or the ones who have the authorised password

class Employee:
    no_of_leaves = 8        # Public variable
    var = 15                # public variable - accessable to anyone
    _protect = 10           # protected variable - only accessable by base class and inherited class - starts with '_'
    __private = 20          # private variable - only accessable to base class - starts with '__'

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Employee name is {self.name}. Salary is {self.salary}. Role is {self.role}."

    @classmethod      
    def change_leaves(cls, new_leaves):         
        cls.no_of_leaves = new_leaves
        
    @classmethod       
    def from_str(cls, str1):
        return cls(*str1.split("-"))

    @staticmethod
    def simple_func(str2):
        return ("This is a STATIC-METHOD " + str2)

lovish = Employee("Lovish", 45000, "Coder")
print(lovish.no_of_leaves)
print(lovish._protect)
# print(lovish.__private)                 # will show error, as python will not allow anyone to access a private variable as such
# to access a private variable need to use  '_<class-name>__<private-variable-name>'
print(lovish._Employee__private)