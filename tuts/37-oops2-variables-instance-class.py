# difference in instance & class variables

class Employee:
    no_of_leaves = 8


rahul = Employee()
lovish = Employee()

rahul.name = "Rahul"
rahul.salary = 45000
rahul.role = "Coder"

lovish.name = "Lovish"
lovish.salary = 75000
lovish.role = "Manager"

print(rahul.name)                       # instance variables
print(rahul.no_of_leaves)               # class variables
print(Employee.no_of_leaves)            # class variables

print(Employee.__dict__)
print(rahul.__dict__)
rahul.no_of_leaves = 10                 # change only instance variable value
print(rahul.no_of_leaves)
print(Employee.no_of_leaves)            # class variable remains the same
print(rahul.__dict__)                   # instance variable (no_of_leaves) gets added

print(lovish.__dict__)
Employee.no_of_leaves = 15              # change a class variable value
print(Employee.__dict__)
print(lovish.no_of_leaves)
print(rahul.no_of_leaves)               # instance variable value takes president over class variable value