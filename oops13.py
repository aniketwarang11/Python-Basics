class A :
    def met(self):
        print("in class A")
class B(A) :
    def met(self):
        print("in class B")
class C (A):
    def met(self):
        print("in class C")
class D (B, C):
    def met(self):
        print("in class D")

a = A()
b = B()
c = C()
d = D()
d.met()