import datetime
from pygame import mixer
import time

def playing_alarm(msg, alarm_file):

    mixer.init()
    mixer.music.load(alarm_file)
    mixer.music.set_volume(0.7)
    mixer.music.play()

    while True:
        user_input=input("Press 's' to stop alarm and 'q' for quit")
        if user_input == "s" or user_input == "S":
            mixer.music.stop()

        elif user_input == "q" or user_input == "Q":
            with open("my_health_logs.txt", "a") as sif:
                sif.write("\n\n")
            quit("Health Remainder Is STOPPED")

        else:
            print("Invalid Input!")
        break

    with open("my_health_logs.txt", "a") as f:
        f.write(f"{msg} on {datetime.datetime.now()}\n")

if __name__ == '__main__':
    print("WELCOME\n\nI am your own health alarm, I'm ready to take your health responsibility.\n")
    print("Instructions\n1. Water alarm will be activated after completion of 30 min.\n2. Eye exercise alarm will be activated after completion of 45 min.\n3. Simple physical exercise alarm will be activated after completion of 60 min.")
    user_name=input("What is your name: ")
    with open("my_health_logs.txt", "a") as hif:
        hif.write(f"*************** This is the health log of user {user_name} ***************\n\n")
    print("\nHealth Remainder Is STARTED")
    water_time = time.time()
    eye_time = time.time()
    exercise_time = time.time()

    while True:
        if time.time() - water_time >= 60*30:
            water_msg = f"{user_name} you drunked water"
            playing_alarm(water_msg, "water_alarm.mp3")
            water_time = time.time()

        if time.time() - eye_time >= 60*45:
            eye_msg = f"{user_name} your eye exercise is done"
            playing_alarm(eye_msg, "eye_alarm.mp3")
            eye_time = time.time()

        if time.time() - exercise_time >= 60*60:
            phy_msg = f"{user_name} your physical exercise is done"
            playing_alarm(phy_msg, "exercise_alarm.mp3")
            exercise_time = time.time()

