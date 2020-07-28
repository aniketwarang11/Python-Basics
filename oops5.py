class Employee :
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod # can only access class variable
    def change_leaves(cls,new_leaves): #we can access this by instance or by class
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_star(cls,string):
        # params = string.split("*")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("*"))

    def printDetails(self):
        return  f" The name is {self.name},Salary is {self.salary} and role is {self.role}"

harry = Employee("Harry",345,"Instructor")
rohan = Employee("Rohan",455,"Student")

karan = Employee.from_star("Karan*200*Instructor") # parse string

Employee.no_of_leaves = 89 # first this will search for instance variable then will go to class variable
harry.change_leaves(34)
print(karan.salary)
