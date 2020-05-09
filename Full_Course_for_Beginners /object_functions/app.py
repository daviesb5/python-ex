# https://youtu.be/rfscVS0vtbw

# Classes and objects allow us to create our own data types
# Objects are created from classes

# from *file* import *class*
from student import Student

student1 = Student("Liam", "Smith", "Business", 3.1, False)
student2 = Student("Emma", "Johnson", "Art", 2.5, True)

# determine whether student1 is on Honor Roll
print(student1.on_honor_roll())