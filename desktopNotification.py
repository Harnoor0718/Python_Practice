import time
from plyer import notification
import winsound
import pyttsx3

engine = pyttsx3.init()

def remind():
    notification.notify(
        title = "Hey Harnoor, Drink Water",
        message = "It's important to stay hydrated. Please drink a glass of water now!",
        timeout = 10
    )   

    winsound.Beep(1000,500)

    engine.say("Hey Harnoor, Drink Water")
    engine.runAndWait()

while True:
    remind()
    time.sleep(60*60)