import time, subprocess, os

timeLeft = 2
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
print(os.getcwd())
subprocess.Popen(['start', 'tyler.mp3'], shell=True)
