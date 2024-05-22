import subprocess

def main() :
    print(subprocess.run(['python', 'tm_bmp.py'], capture_output=True, text=True).stdout)

main()