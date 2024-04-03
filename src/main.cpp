//DEPLOYMENT SYSTEM V.1.0
//FOR:THAILAND CANSAT ROCKET COMPETITION 2024 
//AUTHER: PATARADANAI AKKRATCH 
//TEAM: SKY'S ACE

#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Servo.h>
//G ~= 10m/s^2
Adafruit_MPU6050 mpu;
Servo deployServo;
const float Lunch_threshold = 20.0; // G force threshold from all axis
bool Lunch_state = false;
bool Apogee_state = false;
bool Normal_eject = false;
bool Emergency_eject = false;
unsigned long start_time; // Variable to store the start time

void Check_module(){
    // MPU6050
    if (!mpu.begin()) {
      Serial.println("Failed to find MPU6050 chip");
      while (1) {
        delay(10);
      }
    }
    Serial.println("Found MPU6050");
    // END MPU6050
}
void Eject() {
  deployServo.write(0); 
}
void Lunching(bool* pNormal_eject, bool* pEmergency_eject){
  while(!(*pNormal_eject || *pEmergency_eject)){
      sensors_event_t a, g, temp;
     mpu.getEvent(&a, &g, &temp);  
    float a_xandy = sqrt(a.acceleration.x * a.acceleration.x + a.acceleration.y * a.acceleration.y); //sqrt(ax^2+ay^2)
    if ((millis() - start_time) > 10000){ //set emergency time more than 10sec
      Eject();
      *pEmergency_eject = true;
      *pNormal_eject = false;
    }
    else if ((a_xandy>=10)&&(millis() - start_time>7500)){ //set time threshold more than 7.5 sec
        Eject();
        *pNormal_eject = true;
        *pEmergency_eject = false;

        }
    Serial.println(a_xandy);
    Serial.println((millis() - start_time) / 1000);
  }
}
void setup() {
  Serial.begin(115200);
  Check_module();
  deployServo.attach(9); // Servo attached to pin 9
  deployServo.write(90);  // Set Servo to start position
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);  
  float acceleration = sqrt(a.acceleration.x * a.acceleration.x + a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z);
  Serial.println(acceleration);
  
  if (acceleration >= Lunch_threshold) {
    Lunch_state = true;
    start_time = millis(); // Initialize start time
    Lunching(&Normal_eject, &Emergency_eject);
    while(1){
      if (Emergency_eject) Serial.println("Emergency_eject");
      else  Serial.println("Normal_eject");
      delay(500);
    }
  }
  delay(100); // Delay for stability
}