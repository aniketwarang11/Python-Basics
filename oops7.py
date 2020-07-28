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
    @staticmethod # can be use by this class
    def print_good (stri) :
        print("This is good ",stri)
        return "Whhhooooo"

    def printDetails(self):
        return  f" The name is {self.name},Salary is {self.salary} and role is {self.role}"

#============Inharitance================#
class Programmers (Employee) :
    def __init__(self, aname, asalary, arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages
    def print_prog (self) :
        return f"Name of programmer is {self.name} salery is {self.salary} role is {self.role} languages are {self.languages}"

harry = Employee("Harry",345,"Instructor")
rohan = Employee("Rohan",455,"Student")

karan = Employee.from_star("Karan*200*Instructor") # parse string
rahul = Programmers("Rahul",23456,"Instructor",["python"])


Employee.no_of_leaves = 89 # first this will search for instance variable then will go to class variable
harry.change_leaves(34)
# print(karan.salary)
# print(rahul.print_prog())
#print(harry.print_good("harry"))

# harry.print_good("harry")
Employee.print_good("aniket")