# Healt Management System
# 3 clients - Harry , Rohan and Hammad
# Total 6 files

def getdata () :
    import datetime
    current_time = datetime.datetime.now()
    return current_time.strftime("\n [ %d-%b-%Y (%H : %M : %S :%f)]  ->  ")

real_time = getdata()

# This function is used to store Exercise and Diet of the user
def input_function () :
    print("Which client data you want to Store")
    print(" enter 1 for Harry's Data \n enter 2 for Rohan's Data \n enter 3 for Hammad's Data \n 4 to Exit")
    name1 = int(input())
    if name1 == 1 :
        print("Harry's diet and exercise")
        print(" To store Exercise enter :- 1\n To store Diet enter :- 2")
        store1 = int(input())
        if store1 == 1 :
            print("Storing Harry's Exercise")
            print("enter name of exercise which is done by Harry :- ")
            exercise_done_by_harry = str(input())
            print(exercise_done_by_harry," is Stored")
            #list = [real_time,exercise_done]
            with open("harryexercise.txt","a") as open_Harry_Exercise :
                open_Harry_Exercise.write(real_time)
                open_Harry_Exercise.write(exercise_done_by_harry)
            input_function()
                # print(open_Harry_Exercise.readline())
        else :
            print("Storing Harry's Diet")
            print("enter name of food eaten by Harry")
            food_eaten_by_harry = str(input())
            print(food_eaten_by_harry, " is Stored")
            with open ("harrydiet.txt" , "a") as open_Harry_Diet :
                open_Harry_Diet.write(real_time)
                open_Harry_Diet.write(food_eaten_by_harry)
            input_function()


    elif name1 == 2 :
        print("Rohan's diet and exercise")
        print(" To store Exercise enter :- 1\n To store Diet enter :- 2")
        store2 = int(input())
        if store2 == 1 :
            print("Storing Rohan's Exercise")
            print("enter name of exercise which is done by Rohan :- ")
            exercise_done_by_rohan = str(input())
            print(exercise_done_by_rohan , " is Stored")
            # list = [real_time,exercise_done]
            with open("rohanexercise.txt", "a") as open_Rohan_Exercise:
                open_Rohan_Exercise.write(real_time)
                open_Rohan_Exercise.write(exercise_done_by_rohan)
            input_function()
        else :
            print("Storing Rohan's Diet")
            print("enter name of food eaten by Rohan")
            food_eaten_by_rohan = str(input())
            print(food_eaten_by_rohan, " is Stored")
            with open("rohandiet.txt", "a") as open_Rohan_Diet:
                open_Rohan_Diet.write(real_time)
                open_Rohan_Diet.write(food_eaten_by_rohan)
            input_function()
    elif name1 == 3 :
        print("Hammad's diet and exercise")
        print(" To store Exercise enter :- 1\n To store Diet enter :- 2")
        store3 = int(input())
        if store3 == 1 :
            print("Storing Hammad's Exercise")
            print("enter name of exercise which is done by Hammad :- ")
            exercise_done_by_hammad = str(input())
            print(exercise_done_by_hammad , " is Stored")
            # list = [real_time,exercise_done]
            with open("hammadexercise.txt", "a") as open_Hammad_Exercise:
                open_Hammad_Exercise.write(real_time)
                open_Hammad_Exercise.write(exercise_done_by_hammad)
            input_function()

        else :
            print("Storing Hammad's Diet")
            print("enter name of food eaten by Hammad")
            food_eaten_by_hammad= str(input())
            print(food_eaten_by_hammad , " is Stored")
            with open("hammaddiet.txt", "a") as open_Harry_Diet:
                open_Harry_Diet.write(real_time)
                open_Harry_Diet.write(food_eaten_by_hammad)
            input_function()
    else :
        print("Thanks for using ' Health Management System 1'")



# this function is used to retrive the data

def retrive_function () :
    print("Which client data you want to Retrive")
    print(" enter 1 to retrive Harry's Data \n enter 2 to retrive Rohan's Data \n enter 3 to retrive Hammad's Data \n 4 to Exit")
    name2 = int(input())
    if name2 == 1:
        print("Harry's data")
        print(" To retrive Exercise data enter :- 1\n To retrive Diet data enter :- 2")
        retrive1 = int(input())

        if retrive1 == 1 :
            print("Harry's exercise data is as followes :- \n")
            with open("harryexercise.txt", "r") as open_Harry_Exercise :
                for i in open_Harry_Exercise :
                    print(i,end="")
                print()
               # print(open_Harry_Exercise.readlines())
            retrive_function()
        else :
            print("Harry's diet data is as followes :- \n")
            with open("harrydiet.txt", "r") as open_Harry_Diet:
                for i in open_Harry_Diet :
                    print(i,end="")
                print()
                #print(open_Harry_Diet.readlines())
            retrive_function()

    elif name2 == 2:
        print("Rohan's data")
        print(" To retrive Exercise data enter :- 1\n To retrive Diet data enter :- 2")
        retrive1 = int(input())

        if retrive1 == 1 :
            print("Rohan's exercise data is as followes :- \n")
            with open("rohamexercise.txt", "r") as open_Rohan_Exercise :
                for i in open_Rohan_Exercise :
                    print(i,end="")
                print()
               #print(open_Rohan_Exercise.readlines())
            retrive_function()
        else :
            print("Harry's diet data is as followes :- \n")
            with open("rohandiet.txt", "r") as open_Rohan_Diet:
                for i in open_Rohan_Diet :
                    print(i,end="")
                print()
                #print(open_Rohan_Diet.readlines())
            retrive_function()

    if name2 == 3:
        print("Hammad's data")
        print(" To retrive Exercise data enter :- 1\n To retrive Diet data enter :- 2")
        retrive1 = int(input())

        if retrive1 == 1 :
            print("Hammad's exercise data is as followes :- \n")
            with open("hammadexercise.txt", "r") as open_Hammad_Exercise :
                for i in open_Hammad_Exercise :
                    print(i,end="")
                print()
               #print(open_Hammad_Exercise.readlines())
            retrive_function()
        else :
            print("Hammad's diet data is as followes :- \n")
            with open("hammaddiet.txt", "r") as open_Hammad_Diet:
                for i in open_Hammad_Diet :
                    print(i,end="")
                print()
                #print(open_Hammad_Diet.readline())
            retrive_function()

    else :
        print("Thanks for using ' Health Management System 2'")



def storing_retriving_function () :
    print("If you want to Store data enter 1 \nIf you want to Retrive data enter 2 \nTo guess again enter 3")
    store_retrive = int(input())
    if store_retrive == 1 :
        input_function()
    elif store_retrive == 2 :
        retrive_function()
    else :
        storing_retriving_function()

storing_retriving_function()





