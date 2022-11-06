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
import picamera
from time import sleep
from picamera import PiCamera
from time import sleep
lcd = LCD()

#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer1=18
 
GPIO.setup(buzzer1,GPIO.OUT)
buzzer = Buzzer(18)

driver_name=input("Enter your Name: ")
driver_license=int(input("Enter your Driver License:"))
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(17, 0)
count=0
while(count<20):
    my_input=wiringpi.digitalRead(17)
    if(my_input):
        print("Not Detected !")
  
    else:
        print("Alcohol Detected")
        conn=mysql.connector.connect(host ="localhost", user ="lux", password= "lux", database = "LuxReportDB")
        my_cursor = conn.cursor()

        sql =" INSERT INTO LuxReport(license_ID,driver_name,timer) VALUES(%s,%s,%s)"
    
        val=(driver_license, driver_name, datetime.datetime.now())

        my_cursor.execute(sql, val)

        conn.commit()                     
        print(my_cursor.rowcount,"1 Record Inserted")

        #sql1="SELECT* FROM LuxReport"

        #my_cursor.execute(sql1)

        #print(my_cursor.fetchall())
        camera =PiCamera()
        camera.start_preview()
        camera.start_recording('recorded.h264')
        camera.wait_recording(3)
        camera.stop_recording()
        camera.stop_preview()
        
        def safe_exit(signum, frame):
            exit(1)
            buzzer = Buzzer(18) 
        try:      
            signal(SIGTERM, safe_exit)
            signal(SIGHUP, safe_exit)
            lcd.text("Alcohol,", 1)
            lcd.text("Detected!", 2)
            pause()
            while True:     
                buzzer.on() #Buzzer ON
                sleep(1) #0.5s delay
                buzzer.off() #Buzzer OFF
                sleep(1) #0.5s delay
                buzzer.beep()
        except KeyboardInterrupt:
            pass
        finally:

            lcd.clear()
            
        while True:
            GPIO.output(buzzer1,GPIO.HIGH)
            print ("Beep")
            sleep(0.5) # Delay in seconds
            GPIO.output(buzzer1,GPIO.LOW)
            #print ("No Beep")
            sleep(0.5)
        while True:
            buzzer1.beep()
            
        
        






