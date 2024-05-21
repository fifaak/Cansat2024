import pandas as pd
import subprocess
import time
import nest_asyncio
import asyncio
df = pd.read_csv("./fp.csv")
nest_asyncio.apply()

async def CMD2CODE(cmd):
    print(f"Executing {cmd}")
    await asyncio.sleep(0.1)

def CMD2FREQ(cmd):
    return {
        'tm;mpu;2': 0.1,
        'tm;bmp;2': 1,
        'tm;mcp;2': 1,
        'tm;gps;2': 5
    }[cmd]

async def execute_task(cmd):
    while True:
        await CMD2CODE(cmd)
        await asyncio.sleep(CMD2FREQ(cmd))

async def main():
    tasks = [
        execute_task('tm;mpu;2'),
        execute_task('tm;bmp;2'),
        execute_task('tm;mcp;2'),
        execute_task('tm;gps;2')
    ]
    await asyncio.gather(*tasks)

await main()