#This is Buzzer Program

from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(18) #Define GPIO23 as buzzer

while True:
    buzzer.on() #Buzzer ON
    sleep(1) #0.5s delay
    buzzer.off() #Buzzer OFF
    sleep(1) #0.5s delay
while True:
    buzzer.beep()