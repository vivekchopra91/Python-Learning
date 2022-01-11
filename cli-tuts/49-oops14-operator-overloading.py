class Employee:
    no_of_leaves = 8

    # init dunder method
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Employee name is {self.name}. Salary is {self.salary}. Role is {self.role}."

    @classmethod      
    def change_leaves(cls, new_leaves):         
        cls.no_of_leaves = new_leaves
    
    # dunder add method --> helps is operator overloading
    def __add__(self, other):
        return self.salary + other.salary

    # dunder true division method
    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self) -> str:
        return f"Employee ('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self) -> str:
        return self.print_details()


lovish = Employee("Lovish", 5000, "Programmer")
rahul = Employee("Rahul", 1000, "Trainee")

print(lovish + rahul)
print(lovish / rahul)

print(lovish)                    # default is str
print(str(lovish))
print(repr(lovish))

print(rahul)                    # default is str 
print(str(rahul))
print(repr(rahul))

# To Try other dunder methods - Maping Operators to Functions