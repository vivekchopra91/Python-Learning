# Class-Method as Alternative-Constructor
class Employee:
    no_of_leaves = 8

    # class-constructor
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Employee name is {self.name}. Salary is {self.salary}. Role is {self.role}."

    @classmethod                                # decorator
    def change_leaves(cls, new_leaves):         # changes the class variables
        cls.no_of_leaves = new_leaves
        
    @classmethod                                # alternative-constructor
    def from_str(cls, str1):
        # l1 = str1.split("-")                  # create a list from a string
        # print(l1)                             # output is a list
        # return cls(l1[0], l1[1], l1[2])
        return cls(*str1.split("-"))

rahul = Employee("Rahul", 45000, "Coder")
lovish = Employee("Lovish", 75000, "Manager")
atul = Employee.from_str("Atul-55000-HR")

rahul.change_leaves(15)         # changes the class variables
print(lovish.no_of_leaves)
print(atul.print_details())
print(atul.no_of_leaves)