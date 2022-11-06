#define tempPin  A0                                               // temperature sensor 
#define red  11                                                   // RGB led red
#define green  12                                                // RGB led green
#include <Servo.h>                                               // Servo libary 
Servo myservo;                                                   // to control the servo motor
int pos = 0;                                                     // position starting on 0


void setup() {
  Serial.begin(9600);                                               
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  myservo.attach(3);                                             // servo on pin 3
}

void loop() {
  float value = analogRead(tempPin);
  float tempr = (value * 500) / 1024;                             // calc of temperature in celcius
  Serial.print("Temperature: ");
  Serial.print(tempr);
  Serial.print("*C");
  Serial.println();                                               // it'll show in the serial monitor  
  
  if (tempr <= 40){                                               // less than 40
    digitalWrite(red, LOW);
    digitalWrite(green, HIGH);
    myservo.detach();                                             // stops the servo motor
    
  }
  else if (tempr >= 40){                                          // greater than 40
    digitalWrite(red, HIGH);
    digitalWrite(green, LOW);
    myservo.attach(3);
    myservo.write(pos);                                           // position for the servo to turn
  }
   delay(200); 
  
  for (pos = 0; pos <= 180; pos += 1){                            // go forward 180 degrees
    myservo.write(pos);
    delay(20);
  }
  for (pos = 180; pos <= 0; pos -= 1) {                           // go backward 180 degrees
    myservo.write(pos);
    delay(20);
  }
}                                                                 // loop
