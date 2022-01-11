class Employee:
    no_of_leaves = 8

    # constructor
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Employee name is {self.name}. Salary is {self.salary}. Role is {self.role}."

rahul = Employee("Rahul", 45000, "Coder")                   # all arguments gor to 'init' function inside the class
lovish = Employee("Lovish", 75000, "Manager")

print(rahul.print_details())
print(lovish.salary)
print(lovish.role)