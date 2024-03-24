#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

// Define calibration offsets (adjust based on your sensor calibration)
float accelOffsetX = 0.0;  // X-axis accelerometer offset
float accelOffsetY = 0.0;  // Y-axis accelerometer offset
float accelOffsetZ = 0.0;  // Z-axis accelerometer offset

// Define complementary filter coefficients (adjust based on desired response)
float alpha = 0.95;       // Complementary filter coefficient (0.0 to 1.0)
float gyroYawRateCoef = 0.01; // Scaling coefficient for yaw rate

float roll = 0.0;   // Filtered roll angle (0-180 degrees)
float pitch = 0.0;  // Filtered pitch angle (0-180 degrees)
float yaw = -999.0f; // Initialize yaw to a large negative value for initial handling

// Optional: Yaw offset for calibration (uncomment if using)
// float yawOffset = 0.0; // Set this value after calibration if needed

void calibrateAccel() {
  // Implement your accelerometer calibration routine here (e.g., average multiple readings)
  // Update `accelOffsetX`, `accelOffsetY`, and `accelOffsetZ` with calibration values
  Serial.println("** Perform accelerometer calibration here! **");
}

void setup() {
  Serial.begin(115200); // Set serial communication baud rate (adjust if needed)
  while (!Serial);

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  // Calibrate accelerometer (replace with your calibration routine)
  calibrateAccel();
}

void loop() {
  sensors_event_t a, g, temp;

  mpu.getEvent(&a, &g, &temp);

  // Apply calibration offsets to accelerometer readings
  a.acceleration.x -= accelOffsetX;
  a.acceleration.y -= accelOffsetY;
  a.acceleration.z -= accelOffsetZ;

  // Calculate roll and pitch angles using arctangent with proper handling of singularities
  float y_over_z = a.acceleration.y / (a.acceleration.z + 0.000001f);  // Avoid division by zero
  float x_over_sqrt_yz = a.acceleration.x / sqrt(a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z + 0.000001f);  // Avoid division by zero
  roll = atan2(y_over_z, 1.0f) * 180.0f / PI;
  pitch = atan2(x_over_sqrt_yz, 1.0f) * 180.0f / PI;

  // Complementary filter for yaw (fuses gyroscope and accelerometer data)
  yaw += g.gyro.z * gyroYawRateCoef; // Integrate gyro z-axis reading for yaw rate

  // Constrain yaw to -180 to 180 degrees
  yaw = constrain(yaw, -180.0f, 180.0f);

  // Optional: Apply yaw offset after calibration (uncomment if using)
  // yaw += yawOffset;

  // Complementary filter update
  yaw = alpha * (yaw) + (1.0 - alpha) * roll; // Complementary filter update for yaw

  // Send gyroscope data as comma-separated values (CSV format)
    Serial.print(roll);
  Serial.print(',');
  Serial.print(pitch);
  Serial.print(',');
    Serial.println(yaw);

  delay(100); // Delay between data transmissions (adjust if needed)
}
