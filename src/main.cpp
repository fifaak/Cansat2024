#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Servo.h>
 
Adafruit_MPU6050 mpu;
Servo myServo;

void setup() {
  Serial.begin(115200);
  
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  myServo.attach(9); // Servo attached to pin 9
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  
  // Map accelerometer values to servo range (0-180)
  int servoAngleX = map(a.acceleration.x, -17000, 17000, 0, 180); // Assuming full range of MPU6050
  int servoAngleY = map(a.acceleration.y, -17000, 17000, 0, 180); // Assuming full range of MPU6050
  
  // Limit servo angle to avoid excessive movements
  servoAngleX = constrain(servoAngleX, 0, 180);
  servoAngleY = constrain(servoAngleY, 0, 180);
  float X = a.acceleration.x;
  float Y = a.acceleration.y;
  // Set servo positions
  Serial.println(60-(X*X+Y*Y)*100/180);
  myServo.write(60-(X*X+Y*Y)*100/180);

  
  delay(100); // Delay for stability
}
