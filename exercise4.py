# printing pattrn
# imput = integer n
# boolean = true or fales
# if true than this pattern
# *
# **
# ***
# ****
#
# else this pattern
# ****
# ***
# **
# *

num1 = int (input("Enter no of row you want in patter :- "))
num3 =int( input ("enter 1 for accending pattern and 0 for descending pattern :- "))
num2 = bool(num3)
if num2 == True :
   for i in range(1,num1+1) :
       for j in range (1,i+1) :
           print("*",end="")
       print()
elif num2 == False:
    for i in range (num1,0,-1) : #-1 means start from back
        for j in range(1,i+1):
            print("*", end="")
        print()

# num1 = 4
# for i in range(num1+1) :
#     for j in range (i) :
#         print("*",end="")
#     print()
