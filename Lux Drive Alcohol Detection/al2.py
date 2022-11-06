import time
import datetime
import MySQLdb
import mysql.connector
import wiringpi as wiringpi
from gpiozero import Buzzer
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import picamera
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
camera = picamera.PiCamera()
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=18 
GPIO.setup(buzzer,GPIO.OUT)

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(17, 0)
count=0
while(count<20):
    my_input=wiringpi.digitalRead(17)
    if(my_input):
        print("Not Detected !")
        
    else:
        print("Alcohol Detected")
        camera.start_preview()
        camera.start_recording('recorded1.h264')
        camera.wait_recording(5)
        camera.stop_recording()
        camera.stop_preview()    

        def safe_exit(signum, frame):
            exit(1)
        try:
            signal(SIGTERM, safe_exit)
            signal(SIGHUP, safe_exit)
            lcd.text("Alcohol,", 1)
            lcd.text("Detected", 2)
            pause()
        except KeyboardInterrupt:
            pass
        finally:
            lcd.clear()
            


   
        






