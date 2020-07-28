# guess the no



def guess_the_no () :
    print("Guess the no in 5 turns only")
    n = 18
    i = 1
    while (i < 6) :
        m = int(input("enter a no :- "))
        if m < n :
            print("no is lesser ")
        elif m > n :
            print("no is grater ")
        else :
            print("you found the no")
            print(i ,"no of gusses you took to finish")
            break
        i = i+1
        print("you have ",6-i," guess left")
        if i==6 :
            print("if you want to play again then enter Yes else No")
            newgame = input()
            newgame1 = newgame.capitalize()
            if newgame1 == "Yes":
                guess_the_no()
            else:
                print("game over \n")
                print("thanks for playing")

guess_the_no()
# y=x.capitalize()


