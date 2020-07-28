
print("enter no 1 :- ")
num1 = input()
print("enter no  :- ")
num2 = input()
try:
    print("The sum of these no is :- ", int(num1)+int(num2))
except Exception as e:
    print(e)
print("important")