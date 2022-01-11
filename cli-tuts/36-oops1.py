# Class -> Template(Blank Form)     -> DRY concept ->Do not repeat yourself
# Object -> Matter for template     -> Instance of the class

class Student:
    pass

# assign to a class
rahul = Student()
lovish = Student()

# createing instance variables
rahul.name = "Rahul"
rahul.std = 11
rahul.section = "A"
rahul.subjects = ["Physics", "Chemistry", "Maths", "Physical"]

lovish.name = "Lovish"
lovish.std = 11
lovish.section = "B"
lovish.subjects = ["Physics", "Chemistry", "Maths", "Computer"]

print(rahul.name, lovish.name)
print(rahul.std, lovish.std)
print(rahul.section, lovish.section)
print(rahul.subjects, lovish.subjects)