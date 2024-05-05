import subprocess

eval("subprocess.call(['python', 'enable_mpu.py'])")
subprocess.call(['python', 'enable_gps.py'])
subprocess.call(['python', 'enable_bmp.py'])
subprocess.call(['python', 'enable_mcp.py'])
subprocess.call(['python', 'disable_mpu.py'])
subprocess.call(['python', 'disable_gps.py'])
subprocess.call(['python', 'disable_bmp.py'])
subprocess.call(['python', 'disable_mcp.py'])
subprocess.call(['python', 'tm_mpu.py'])
subprocess.call(['python', 'tm_gps.py'])
subprocess.call(['python', 'tm_bmp.py'])
subprocess.call(['python', 'tm_mcp.py'])