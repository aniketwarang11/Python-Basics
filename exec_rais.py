a = input("What is your name")
b= input("How much do you earn")

if int(b) == 0 :
    raise ZeroDivisionError("b is 0")
if a.isnumeric():
    raise Exception("Numbes are not allowed")
print(f"hello {a}")

#1000 lines taking 1hour