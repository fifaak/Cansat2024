#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Servo.h>

Adafruit_MPU6050 mpu;
Servo deployServo;

// Threshold acceleration for deployment
const float deployThreshold = 30.0; // Adjust as needed

void setup() {
  Serial.begin(115200);
  
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  deployServo.attach(9); // Servo attached to pin 9
  deployServo.write(90); 
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  
  // Calculate total acceleration magnitude
  float acceleration = sqrt(a.acceleration.x * a.acceleration.x +a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z);
  Serial.println(acceleration);
  if (acceleration >= deployThreshold) {
    deployServo.write(0); // Assuming 180 opens the servo

    delay(1000); // Assuming 1 second is enough for deployment
    
    }
    
    delay(100); // Delay for stability
}

// void deployCanSat() {
//   // Open the servo to release the CanSat
//   deployServo.write(180); // Assuming 180 opens the servo
//   delay(1000); // Assuming 1 second is enough for deployment
  
//   // Close the servo after deployment (optional)
//   deployServo.write(0); // Assuming 0 closes the servo
// }
