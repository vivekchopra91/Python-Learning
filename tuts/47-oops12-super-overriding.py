class A:
    class_var1 = "This is a class variable of class A"

    def __init__(self):
        self.var1 = "This is inside class A's constructor"
        self.classvar1 = "This is an instance variable in class A"
        self.classvar2 = "This is another instance variable in class A"

class B(A):
    class_var1 = "This is a class variable of class B"

    def __init__(self):             # this will over-write constructor of class A, also if required to place more variables for class B seperately
        super().__init__()          # this constructor is to be called before asigining more variables for class B
        self.classvar1 = "This is inside constructor of class B"

a = A()
b = B()

print(b.class_var1)
print(b.classvar1)
print(b.classvar2)