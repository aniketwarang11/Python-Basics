from time import time
from datetime import datetime
from pygame import mixer

def musiconloop(file,stopper) :
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True :
        a = input()
        if a == stopper :
            mixer.music.stop()
            break
def log_now(msg) :
    with open("mylogs.txt","a") as f :
        f.write(f"{msg}->{datetime.now()}\n")

if __name__ == '__main__' :
    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersecs = 5
    exsecs = 10
    eyessecs = 20
    while True :
        if time() - init_water > watersecs :
            print("Water drinkind time. Enter 'drank' to stop alarm.")
            musiconloop("water.mp3", "drank")
            init_water = time()
            log_now("Drank water at ")

        if time() - init_eyes > eyessecs :
            print("Eye exercisse time. Enter 'doneeyes' to stop alarm.")
            musiconloop("eyes.m4a", "doneeyes")
            init_eyes = time()
            log_now("Eyes relaxed at ")

        if time() - init_exercise > exsecs :
            print("Physical activity time. Enter 'donephy' to stop alarm.")
            musiconloop("workoutRingtone.m4a", "donephy")
            init_exercise = time()
            log_now("Physical activity done at ")




