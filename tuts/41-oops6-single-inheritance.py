class Employee:
    no_of_leaves = 8

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

class Programmer(Employee):
    def __init__(self, name, salary, role, language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language
    
    def print_new_details(self):        # can give additional details after inheriting from Employee class
        return f"The Programmer's name is {self.name}. Salary is {self.salary}. Role is {self.role}. Programing languages known are {self.language}."

rahul = Employee("Rahul", 45000, "Coder")
rohit = Employee("Rohit", 35000, "Programmer")

lovish = Programmer("Lovish", 75000, "Manager", ["Python"])
atul = Programmer.from_str("Atul-55000-HR-['Python', 'Cpp']")

print(atul.print_details())
print(lovish.print_new_details())
print(atul.language)