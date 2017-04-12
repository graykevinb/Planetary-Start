# This code could be used to run a robot that says hello world or as the name suggests, start ingition for a mars mission.
# Ok maybe this code isn't robust enough for space. :) 
import RPi.GPIO as GPIO
from time import sleep
import os

#Red LED: #19
#Green LED: #21
#Switch: 26

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #Turn Red and Green LED on to signify everythings working.
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)

    sleep(0.6)

    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

    kill_code = 'pkill -f program.py'
    code = 'python3 home/pi/planetary_start/program.py'
    GPIO.output(21, GPIO.LOW)

    #Basically these next three lines and the loop is the main part of this function.
    #Did I just spend a whole line explaining something you already know? I guess I did.
    #Anyways the loop continues waiting for the button to be pressed.
    #If pressed it waits a few seconds and if pressed again begins a poweroff sequence.
    #If it is held it is checked if the target program is running.
    #If it is running the program is shutoff, if not running the program is run.
    f = open('home/pi/planetary_start/hi.txt', 'w')
    program_test = open('home/pi/planetary_start/program_test.txt', 'r+')
    program_on = 'off'

    while True:
        program_on = program_test.read()
        button_input = GPIO.input(26)
        if button_input == False:
            GPIO.output(21, GPIO.HIGH)
            sleep(3)
            button_input = GPIO.input(26)
            if button_input == False:
                program_test.write('off')
                f.write('poweroff\n')
                GPIO.output(21, GPIO.LOW)
                return
            elif program_test == 'off\n' or 'off':
                os.system(code)
                program_test.write('running')
            elif program_test == 'on' or 'on\n':
                pass
            else:
                pass
        GPIO.output(21, GPIO.LOW)


try:
    main()
except:
    GPIO.output(19, GPIO.HIGH)
    sleep(1)
    GPIO.output(19, GPIO.LOW)

GPIO.cleanup()









#See that code down there? I call that the abyss of future code..
#See the CONTRIBUTING file more details.
