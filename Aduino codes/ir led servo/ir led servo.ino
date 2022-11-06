/*[Forwarded from Abrah-Baidoo Stephen]

    1.  If an object is detected, turn the 
      servo motor 10 degrees and turn on the LED
    2.  If there is no object detected, turn the 
      servo motor 150 degrees and turn off the LED
  */
  
  #include <Servo.h>
  Servo Serv;

  int pinIR=2; //IR sensor digital pin
  int pinServo=3; //servo motor pin
  int pinLED=13;
  int val=0;

  void setup(){
    Serv.attach(pinServo);
    pinMode(pinLED,OUTPUT);
  }

  void loop(){
    val = digitalRead(pinIR);
  
    if (val ==0) { 
      Serv.write(180);
      digitalWrite(pinLED,HIGH);
      delay(100);
    }
    else{
      Serv.write(0);
      digitalWrite(pinLED,LOW);
      delay(100);
    }
  }