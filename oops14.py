class Employee :
    no_of_leaves = 10

    def __init__(self, name, salary, role): #this this type of method are called as dunder
        self.name = name
        self.salary = salary
        self.role =role

    def printdetail(self):
        return f"The name is {self.name} salary is {self.salary} role is {self.role}"
    @classmethod
    def change_leaves (cls, newleaves) :
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
       #return self.printdetail()
       return f"Employee('{self.name}',{self.salary},'{self.role}')"

    # def __str__(self):
    #     return f"The name is {self.name} salary is {self.salary} role is {self.role}"



emp1 = Employee("harry",222,"Programmer")
#emp2 = Employee("rohan",22,"cleaner")
#print(emp1)
#print(str(emp1))
print(emp1.printdetail())

