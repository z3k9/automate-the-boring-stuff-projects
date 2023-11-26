import time, subprocess

time_left = 5
while time_left > 0:
    print(time_left, end='')
    time.sleep(1)
    time_left = time_left - 1

subprocess.Popen(['open', '-a', 'iTunes', '~/Desktop/code/automate-the-boring-stuff-projects/alarm.wav'])

