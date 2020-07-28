#your age in 2019
#take age or input from the user and tell them when will they turn 100 year old
#Dont use module like dateime or dateutils
#They can then optionally provide a year and your program must tell their age in that particular year
'''
you should br handeling all sort of errors like :-
1) you are not yet born
2) you seem to be oldest person alive
3) you can also handel other error if possible
'''
current_year = int(input("Enter current Year :-"))
print("Enter your age or Birth year :-")
age = int(input())
if age < 100:
    print ("Your Age is ", age)
    print ("Your birth year is ", current_year-age)
    year_old1 = current_year-age
    print ("You will turn 100 year old in ", year_old1+100)

elif age >1900:
    print ("Your Birth year is ", age)
    print ("Your age is ", current_year-age)

    if current_year - age > 100 and current_year - age < 120:
        print("You are already 100 year old")

    else:
        print ("You will turn 100 year old in ", age+100)

elif age > current_year | age == 0:
    print ("You are not yet born")

elif age >100 and age <120 : #| current_year-age > 100 and current_year-age < 120:
    print ("You are already 100 year old")

else:
    print("You must be dead by now")
