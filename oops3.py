class Employee :
    no_of_leaves = 8
    # this is consructor
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"The name is {self.name},Salary is {self.salary} and role is {self.role}"

# making a object of class Employee
harry = Employee("Harry",345,"Instructor")
print(harry.salary)

# calling method inside Employee class
a = harry.printDetails()
print(a)

