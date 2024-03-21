#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Servo.h>

Adafruit_MPU6050 mpu;
Servo deployServo;
const float Lunch_threshold = 2.0; // G force threshold from all axis
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
void Lunching(sensors_event_t a, bool* pNormal_eject, bool* pEmergency_eject){
  while(!(*pNormal_eject || *pEmergency_eject)){
    if ((millis() - start_time) > 10000){
      Eject();
      *pEmergency_eject = true;
      *pNormal_eject = false;
    }
    int angle = sqrt(a.acceleration.x * a.acceleration.x + a.acceleration.y * a.acceleration.y);
    // Serial.println("Lunching:");
    delay(100);
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
    Lunching(a, &Normal_eject, &Emergency_eject);
    while(1){
      if (Emergency_eject) Serial.println("Emergency_eject");
      else  Serial.println("Normal_eject");
      delay(500);
    }
  }
  delay(100); // Delay for stability
}