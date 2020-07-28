#Rock Paper Sissors game

import random

print("You are Playing Rock Paper Sissor Game")
print()
print("You have to play game 10 times")
# your_choice = str (input("Enter 'R' for Rock \nEnter 'P' for Paper \nEnter 'S' for Sissors\n"))
i = 1
n=10
your_score = 0
comp_score = 0
while i <= n :
    your_choice =  str(input("Enter 'R' for Rock \nEnter 'P' for Paper \nEnter 'S' for Sissors\n"))
    # print("you have to play the game more",n-i,"time")
    choices = ['R','P','S']
    comp_choice = random.choice(choices)

    if your_choice == 'R' :
        if comp_choice == 'P':
            print("Computer choice is :- ",comp_choice)
            print("Computer Win")
            comp_score = comp_score + 1
        elif comp_choice == 'S' :
            print("Computer choice is :- ",comp_choice)
            print("You Win")
            your_score = your_score + 1
        else:
            print("Computer choice is :- ",comp_choice)
            print("Tye")
    elif your_choice == 'P' :
        if comp_choice == 'R':
            print("Computer choice is :- ",comp_choice)
            print("You Win")
            your_score = your_score + 1
        elif comp_choice == 'S' :
            print("Computer choice is :- ",comp_choice)
            print("Computer Win")
            comp_score = comp_score + 1
        else:
            print("Computer choice is :- ",comp_choice)
            print("Tye")
    #your choice is S
    else :
        if comp_choice == 'R':
            print("Computer choice is :- ",comp_choice)
            print("Computer Win")
            comp_score = comp_score + 1
        elif comp_choice == 'P' :
            print("Computer choice is :- ",comp_choice)
            print("You Win")
            your_score = your_score + 1
        else:
            print("Computer choice is :- ",comp_choice)
            print("Tye")
    print("you have to play the game more", n - i, "time")
    i=i+1

print("Your Score is :- ",your_score)
print("Computer score is :- ",comp_score)
if your_score > comp_score :
    print("You Win the Game")
elif your_score == comp_score :
    print("There is a Tye")
else:
    print("Computer Win the Game")




