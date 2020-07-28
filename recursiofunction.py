#recurtion function

# def print2 () :
#     print ("this is harry")
#
# print2()

#Factorial


# def factorial(n ) :
#     facto = 1
#     for i in range (n) :
#         facto = facto * (i+1)
#     return facto
# print("enter a no")
# num = int (input())
# print("factorial is", factorial(num))


# def factorial_recursive(n) :
#
#     return n * factorial_recursive(n-1)
#
# print("factoial using recursion is :- ",factorial_recursive(4))

# def factorial_recursive2(n) :
#     if n == 1 :
#         return  1
#     else:
#         return n*factorial_recursive2(n-1)
#
# num = int (input( "Enter a no :- "))
# print("factorial using recursion ", factorial_recursive2(num))

# febonacci series
# num = int (input("Enter length of febonacci series :- "))

# def febonacci_series1 (n) :
#     a=0
#     b=1
#     print("0", end=" ")
#     print("1", end=" ")
#     for i in range (n -2) :
#         i = a+b
#         print (i,end=" ")
#         a = b
#         b = i

def febonacci_series2( n ) :
    if n <= 1 :
        return  n
    else:
        return febonacci_series2(n-1) + febonacci_series2(n-2)
num = int (input("Enter length of febonacci series :- "))
if num <= 0:
    print("enter postive no")
else:
    print("febonacci series ")
    for i in range (num) :
        print(febonacci_series2(i))



