import subprocess

result = subprocess.run(["python", "enable_mpu.py"], capture_output=True, text=True)

print(result.stdout)
