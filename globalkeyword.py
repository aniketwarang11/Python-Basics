# #global variable
# i = 10 #THIS VARIABLE IS IN GLOBAL SCOPE
#
# def fun_1 (n) :
# #function will always check for local scope first
#     #i = 5 #local variable
#     j = 3
#     global i #this will help to change value of global variable
#     i=i+1
#     print(n," printed")
#     print(i)
#
# fun_1("hello world")


def aniket() :
    x  = 10
    def warang() :
        global x
        x = 100
    print("Before calling warang",x)
    warang()
    print("after calling warang",x)

aniket()