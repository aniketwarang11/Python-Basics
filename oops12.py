class A :
    classvar1 = "I am in class variable in class  A"
    def __init__(self):
        self.var1 = "I an in class A's Constructor"
        self.classvar1 = "Instance variable in class A"
        self.special = "special"

class B(A) :
    classvar1 = "I am in class variable in class  B"
    def __init__(self):
        #super().__init__() #this will go in super constructor but will get override
        self.var1 = "I an in class b's Constructor"
        self.classvar1 = "Instance variable in class B"
        super().__init__() #this will execute the super constructor statement




a = A()
b = B()

print(b.special,b.var1,b.classvar1)