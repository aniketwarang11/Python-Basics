"""
Iterable - __iter__() or __getitem()__()
Itreator - __next__()
Iteration -
"""

def gen(n) :
    for i in range (n) :
        yield i

g = gen (5)

# print (g.__next__())
# print (g.__next__())
# print (g.__next__())
# print (g.__next__())
# print (g.__next__())


# for i in g :
#     print(i)

# h = "Harry"
# ite = iter(h)
# print(ite.__next__())
# print(ite.__next__())
# print(ite.__next__())

# for c in h :
#     print(c)

def fact(n) :
    facto = 1
    for i in range (n) :
        facto = facto * (i+1)
        yield facto

f = fact(6)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

# for i in f :
#     print (i)

def febo(n) :
    a = 0
    b=1
    print("0")
    print("1")
    for i in range (n -2) :
        i = a+b
        yield i
        a = b
        b = i

fe = febo(10)
# print(fe.__next__())
# print(fe.__next__())
# print(fe.__next__())
# print(fe.__next__())

for i in fe :
    print(i)



