//TEST ONLY
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Servo.h>

Adafruit_MPU6050 mpu;
Servo deployServo;

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
}