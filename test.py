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

while(1):
    CMD2CODE('tm;mpu;2')
    time.sleep(CMD2FREQ('tm;mpu;2'))
    
while(1):
    CMD2CODE('tm;bmp;2')
    time.sleep(CMD2FREQ('tm;bmp;2'))

while(1):
    CMD2CODE('tm;mcp;2')
    time.sleep(CMD2FREQ('tm;mcp;2'))

while(1):
    CMD2CODE('tm;gps;2')
    time.sleep(CMD2FREQ('tm;gps;2'))