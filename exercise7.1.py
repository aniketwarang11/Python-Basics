import datetime
import pygame


pygame.init()

water = 'water.mp3'
eyes = 'eyes.mp3'
physical = 'physical.mp3'
your_name = input("Enter your name :- ")
print(f"{your_name.capitalize()} welcome to the office")

file = your_name

water_alarm = 40 #minute
eyes_alarm = 30 #minute
physical_alarm = 45 #minute\

ex = True

d = datetime.datetime.now()
water_timer = d.minute + water_alarm
eyes_timer = d.minute + eyes_alarm
physical_timer = d.minute + physical_alarm

_file = open(file,"a")
print(d)

while ex != False :
    new_d = datetime.datetime.now()
    # print("in while")
    if water_timer >= 60 or eyes_timer >= 60 or physical_timer >= 60 :
        if water_timer >= 60 :
            water_timer  -= 60
            d = datetime.datetime.now()
            minute = d.minute

        if eyes_timer >= 60 :
            eyes_timer  -= 60
            d = datetime.datetime.now()
            minute = d.minute

        if physical_timer >= 60 :
            physical_timer  -= 60
            d = datetime.datetime.now()
            minute = d.minute

    else:
        if new_d.minute == water_timer :
            print("Please drink water",new_d)
            # pygame.mixer.music.load(water)
            # pygame.mixer.music.play()
            _input = input("Enter drank if you drank water")
            if _input.lower() == 'drank' :
                # pygame.mixer.music.stop()
                _file.write(f"Drank water at :- {datetime.datetime.now()}\n\n")
                water_timer = d.minute + water_alarm

        elif new_d.minute == eyes_timer :
            print("Please d0 some eyes exercise",new_d)
            # pygame.mixer.music.load(eyes)
            # pygame.mixer.music.play()
            _input = input("Enter Eyesdone if you did the exercise")
            if _input.lower() == 'eyesdone' :
                # pygame.mixer.music.stop()
                _file.write(f"Eyes exercise done at :- {datetime.datetime.now()}\n\n")
                eyes_timer = d.minute + eyes_alarm

        elif new_d.minute == physical_timer :
            print("Please do some physical exercise",new_d)
            # pygame.mixer.music.load(physical)
            # pygame.mixer.music.play()
            _input = input("Enter Exercisedone if you did the Exercise")
            if _input.lower() == 'exercisedone' :
                # pygame.mixer.music.stop()
                _file.write(f"Exercise dine at :- {datetime.datetime.now()}\n\n")
                physical_timer = d.minute + physical_alarm

_file.close()
