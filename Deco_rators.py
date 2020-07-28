# def func1 () :
#     print("Aniket")
# func2 = func1
# del func1
# func2()



# def func_ret (num) :
#     if num == 0:
#         return  print
#     if num == 1:
#         return sum
# a = func_ret(1)
# print(a)

# def executor(func) :
#     func("this")
#
# executor(print)

def dec1(func1) :
    def nowexec():
        print("Executing now")
        func1()
        print("executed")
    return nowexec
@dec1
def who_is_aniket ():
    print("Aniket is a good boy")

#who_is_aniket = dec1(who_is_aniket) # this is same as @dec1
who_is_aniket()

