import subprocess
import nest_asyncio
import asyncio

nest_asyncio.apply()

async def CODE(cmd):
    print(f"Executing {cmd}")
    await asyncio.sleep(0.1)

def module(cmd):
    if cmd == 'tm;mpu;2':
        return subprocess.run(['python', 'tm_mpu.py'], capture_output=True, text=True).stdout
    elif cmd == 'tm;bmp;2':
        return subprocess.run(['python', 'tm_bmp.py'], capture_output=True, text=True).stdout
    elif cmd == 'tm;gps;2':
        return subprocess.run(['python', 'tm_gps.py'], capture_output=True, text=True).stdout
    elif cmd == 'tm;mcp;2':
        return subprocess.run(['python', 'tm_mcp.py'], capture_output=True, text=True).stdout

def CMD2FREQ(cmd):
    return {
        'tm;mpu;2': 0.1,
        'tm;bmp;2': 1,
        'tm;mcp;2': 1,
        'tm;gps;2': 5
    }[cmd]

async def execute_task(cmd):
    while True:
        await CODE(cmd)
        result = module(cmd)
        print(result)
        await asyncio.sleep(CMD2FREQ(cmd))

async def main():
    tasks = [
        execute_task('tm;mpu;2'),
        execute_task('tm;bmp;2'),
        execute_task('tm;mcp;2'),
        execute_task('tm;gps;2')
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
