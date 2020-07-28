"""
i =0
while (True):
    if i+1<=5 :
        i=i+1
        continue
    print(i + 1 , end = " ")
    if (i == 10) :
       break
    i = i + 1

"""
"""
var1 = int (input("Enter a no"))
while var1 < 100 :
    print ("enter no grater than 100")
    var1 = int (input("enter no"))
    if var1 >100 :
        print("no is grater than 100")
"""
while(True):
    inp = float(input("enter a no :- "))
    if inp > 100:
        print("no is gtarer than 100")
        break
    else:
        print("try again!")
        continue

