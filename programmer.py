# Programmer health
# office starting & closing time - DONE
# drink water, do exercise and do eye_exercise - DONE
# at least drink 3.5 Litres = Every 30 min till office closes - DONE
# do eye exercise after every 45 minutes - done
# do exercise after every 60 minutes - done
# Add, audio when we the time is to do anything specific = pygame - done
# Type "Done" or something to close the music - done
# log everytime when you enter Done - done
# there should be three files for each option - done
# MADE BY @ELDERNY1 on telegram

import time
from pygame import mixer

def gettime():
    import datetime
    return datetime.datetime.now()

date = str(gettime())

print("\nWelcome Programmer, MADE BY ELDERNY")
time_input = time.strftime("%H")
currenttime = int(time_input)
start = int(input("Please type the Starting Hour of your office, like '9' as an hour \n" + "Opening Time: "))
end = int(input("Please type the Ending Hour of your office, like '17' as an hour \n" + "Closing Time: "))
water_required = 10
eye_exercise = 10
exercise_required = 10
water_waiting = 1800
eye_waiting = 2700
exercise_waiting = 3600
water_time = time.time()
eye_time = time.time()
exercise_time = time.time()
print("\nProgram Will start in 1 min! :)")
while(True):
    if currenttime >= start and currenttime <= end:
        time.sleep(60)
        if water_required > 0:
            if time.time() - water_time > water_waiting:
                print("You got Water to drink")
                while(True):
                    def water_music():
                        mixer.init()
                        mixer.music.load("water.mp3")
                        mixer.music.set_volume(0.7)
                        mixer.music.play(-1)
                    water_music = water_music()
                    ask = input("Type 'drank' to stop the music if you Drank the Water\n" + "Type Here: ").lower()
                    if ask == "drank":
                        print("Log Added to water.txt :)")
                        with open("water.txt", "a") as f:
                            water_time = time.time()
                            a = f.write("Current Time: " + date + " Drank Water\n")
                            water_required = water_required - 1
                            break
        if eye_exercise > 0:
            if time.time() - eye_time > eye_waiting:
                print("You Need to do Eye Exercises")
                while (True):
                    def eye_music():
                        mixer.init()
                        mixer.music.load("eyes.mp3")
                        mixer.music.set_volume(0.7)
                        mixer.music.play(-1)
                    eye_music = eye_music()
                    ask = input("Type 'Done' to stop the music if you did eye exercise\n" + "Type Here: ").lower()
                    if ask == "done":
                        print("Log Added to eye.txt :)")
                        with open("eye.txt", "a") as f:
                            eye_time = time.time()
                            a = f.write("Current Time: " + date + " Exercised Eye\n")
                            eye_exercise = eye_exercise - 1
                            break
        if exercise_required > 0:
            if time.time() - exercise_time > exercise_waiting:
                print("You need to do Exercises")
                while (True):
                    def exercise_music():
                        mixer.init()
                        mixer.music.load("exercise.mp3")
                        mixer.music.set_volume(0.7)
                        mixer.music.play(-1)
                    exercise_music = exercise_music()
                    ask = input("Type 'Finish' to stop the music if you did exercises\n" + "Type Here: ").lower()
                    if ask == "finish":
                        print("Log Added to exercise.txt :)")
                        with open("exercise.txt", "a") as f:
                            exercise_time = time.time()
                            a = f.write("Current Time: " + date + " Exercise Done\n")
                            exercise_required = exercise_required - 1
                            break
        else:
            print("BREAK!!")
            break
    if end > 24:
        print("Alien xD")
        break
    else:
        if exercise_required <= 1:
            print("Work done")
        else:
            print("Out of Time Zone")
            break
