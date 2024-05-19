import pandas as pd
import subprocess
import time
df = pd.read_csv("./fp.csv")

def CMD2TASK(cmd):
    mapping = dict(zip(df['CMD'], df['TASK']))
    return mapping.get(cmd, "Task not found")
def CMD2CODE(cmd):
    mapping = dict(zip(df['CMD'], df['CODE']))
    return eval(mapping.get(cmd, "Code not found"))
def CMD2FREQ(cmd):
    mapping = dict(zip(df['CMD'], df['FREQUENCY']))
    return mapping.get(cmd, "Frequency not found")

# Initialize the next scheduled times
next_time_mpu = time.time()
next_time_bmp = time.time()
next_time_mcp = time.time()
next_time_gps = time.time()

while True:
    current_time = time.time()

    if current_time >= next_time_mpu:
        CMD2CODE('tm;mpu;2')
        next_time_mpu = current_time + CMD2FREQ('tm;mpu;2')

    if current_time >= next_time_bmp:
        CMD2CODE('tm;bmp;2')
        next_time_bmp = current_time + CMD2FREQ('tm;bmp;2')

    if current_time >= next_time_mcp:
        CMD2CODE('tm;mcp;2')
        next_time_mcp = current_time + CMD2FREQ('tm;mcp;2')

    if current_time >= next_time_gps:
        CMD2CODE('tm;gps;2')
        next_time_gps = current_time + CMD2FREQ('tm;gps;2')

    # Small sleep to avoid busy-waiting
    time.sleep(0.01)