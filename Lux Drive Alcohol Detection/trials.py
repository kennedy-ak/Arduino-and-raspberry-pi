import time
import datetime
import MySQLdb
import mysql.connector
import wiringpi as wiringpi
from gpiozero import Buzzer
from time import sleep
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import RPi.GPIO as GPIO
from time import sleep
lcd = LCD()
buzzer = Buzzer(17) #Define GPIO23 as buzzer
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=17 
GPIO.setup(buzzer,GPIO.OUT)

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(25, 0)
count=0
while(count<20):
    my_input=wiringpi.digitalRead(25)

    if(my_input):
        print("Alcohol Detected")    
        def safe_exit(signum, frame):
            exit(1)
        try:
            signal(SIGTERM, safe_exit)
            signal(SIGHUP, safe_exit)
            lcd.text("Alcohol,", 1)
            lcd.text("Detected!", 2)
            pause()
        except KeyboardInterrupt:
            pass
        finally:
            lcd.clear()
        while True:
            GPIO.output(buzzer,GPIO.HIGH)
            print ("Beep")
            sleep(0.5) # Delay in seconds
            GPIO.output(buzzer,GPIO.LOW)
            #print ("No Beep")
            sleep(0.5)
        while True:
            buzzer.beep()
            
        def safe_exit(signum, frame):
            exit(1)
        try:
            signal(SIGTERM, safe_exit)
            signal(SIGHUP, safe_exit)
            lcd.text("Alcohol,", 1)
            lcd.text("Detected!", 2)
            pause()
        except KeyboardInterrupt:
            pass
        finally:
            lcd.clear()
   
    else:
        print("Not Detected !")
        def safe_exit(signum, frame):
            exit(1)
        try:
            signal(SIGTERM, safe_exit)
            signal(SIGHUP, safe_exit)
            lcd.text("Alcohol,", 1)
            lcd.text("Not Detected!", 2)
            pause()
        except KeyboardInterrupt:
            pass
        finally:
            lcd.clear()





