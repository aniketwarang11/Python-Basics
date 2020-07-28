#Healthy Programmer
import time
import datetime
from multiprocessing import process

# 9am - 5pm
# water - water.mp3 (3.5 liters) - Drank - log
# eye - eye.mp3 - every 30 min - Eyesdone - log
# physical activity - physical.mp3 - every 45 min - exdone -lo
# print(mp.cup_count())

print("Healty Programmer")
def getdata () :
    current_time = datetime.datetime.now()
    return current_time.strftime("\n [ %d-%b-%Y (%H : %M : %S :%f)]  ->  ")
real_time = getdata()

def healty_programmer () :
    d = datetime.datetime.now()
    water_alarm = 1 # minute
    eyes_alarm = 2  # minute
    physical_alarm = 3  # minute\

    while True :
        # print('in while')
        new_d = datetime.datetime.now()
        if d.minute + water_alarm == new_d.minute :
        # def water ():
            print("Please Drink Water")
            print("Type 'Drank' if you have drank the water :- ")
            water = str(input())
            if water == "Drank" :
                with open("water.txt", "a") as water_drank:
                    water_drank.write(real_time)
                    water_drank.write(water)
                    break
                    # time.sleep(2)

            else :
                print("Drink water time to time for better helth")
                break
                # time.sleep(2)

        elif d.minute + eyes_alarm == new_d.minute :
        # def eyes () :
            print("Close your eyes for some time")
            print("Type 'Eyesdone' if you have colsed your eyes for some time :- ")
            eyes = str(input())
            if eyes == "Eyesdone" :
                with open("eyes.txt", "a") as eyes_ex:
                    eyes_ex.write(real_time)
                    eyes_ex.write(eyes)
                # time.sleep(3)
            else:
                print("Closing eyes is good for your eyes")
                # time.sleep(3)


        elif d.minute + physical_alarm == new_d.minute:
        # def physical_ex () :
            print("Do some physical exercise")
            print("Type 'Exdone' if you did the exercise :- ")
            exercise = str(input())
            if exercise == "Exdone" :
                with open("physical.txt", "a") as physical_ex:
                    physical_ex.write(real_time)
                    physical_ex.write(exercise)
                # time.sleep(2)
            else:
                print("Do some exercise in regular interval for better helth")


healty_programmer()