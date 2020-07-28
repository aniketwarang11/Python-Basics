#exercise 2 = Faulty calculator

# Design a calculator which will correctly solve the problems except the
#following ones :-

# 45*3 = 555 , 56+9 = 77, 56/6 = 4

#operatir and two no should be taken from user and return the result


print ("Enter two no for computation")
num1 = int(input())
num2 = int(input())
print("which operation do you want to do :- "

      " '*' for multiplication"
      " '+' for addition"
      " '-' for substraction"
      " '/' for division")
operation = input()
if num1 == 45 and num2 == 3 and operation == "*" :
    print("555")
elif num1 == 56 and num2 == 9 and operation == "+" :
    print("77")
elif num1 == 56 and num2 == 6 and operation == "/" :
    print("4")
elif operation == "*" :
    print(num1 * num2)
elif operation == "+" :
    print(num1 + num2)
elif operation == "-" :
    print(num1 - num2)
elif operation == "/" :
    print(num1 / num2)
else:
    print("Wrong operator")


