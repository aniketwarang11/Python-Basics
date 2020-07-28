class Employee :
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    @classmethod # can only access class variable

    def change_leaves(cls,new_leaves):
        #we can access this by instance or by class
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
        #print(f"name is {x}")
        return  f" The name is {self.name},Salary is {self.salary} and role is {self.role}"

#============Inharitance================#

class Player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printDetails(self):
        return f"the name is {self.name} , Game is {self.game}"

class Cool_Programmer(Player,Employee,) :
    pass

harry = Employee("Harry",345,"Instructor")
rohan = Employee("Rohan",455,"Student")

shubham = Player("Shubham",["Cricket"])

karan = Cool_Programmer("Karan",["cricket"])

#print(karan.print_Details())
#print(Employee.printDetails("Aniket"))
Employee.change_leaves(10)
print(Employee.no_of_leaves)