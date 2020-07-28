
#object intospection meaning = to know everything about objects


class Employee :
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):

        return f"The Employee is {self.fname} {self.lname}"
    @property # if you dont want to use '()'
    def email(self):
        if self.fname == None or self.lname == None :
            return "Email is not set plz set it using setter"
        return  f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,st):
        name = st.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf =Employee("Skill", "F")
#print(skillf.email)
#print(type(skillf))
#print(id ("this"))
a="Aniket"
#print(dir(a))

import inspect
print(inspect.getmembers(skillf))