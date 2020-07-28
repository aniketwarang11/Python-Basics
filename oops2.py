class Employee :
    no_of_leaves = 8
    pass
harry = Employee()
rohan = Employee()

harry.name = "harry"
harry.salary = 445
harry.role = "Instructor"

rohan.name = "rohan"
rohan.salary = 4453
rohan.role = "Student"
print(harry.__dict__)
print(rohan.__dict__)

print(harry.no_of_leaves)