a = 2
b = 3
c = sum((2,3)) # built in function
print(c)

def add() :
    print("You are in function 1")

add()
def avg(a,b) :
    """This will calculate average"""
    avg = (a+b)/2
    print(avg)
    return  avg

#v = avg(2,4)
#print(v)
print(avg.__doc__)

