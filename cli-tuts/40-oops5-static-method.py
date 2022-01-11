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

    @staticmethod                   # simple method which does not rely on instance or class variables
    def simple_func(str2):
        return ("This is a STATIC-METHOD " + str2)

rahul = Employee("Rahul", 45000, "Coder")
lovish = Employee("Lovish", 75000, "Manager")
atul = Employee.from_str("Atul-55000-HR")


print(atul.simple_func("Of Python OOPS tutorial."))
print(Employee.simple_func("showing another example using Employee class."))