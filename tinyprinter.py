#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

def toggle():
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(20, GPIO.LOW)

def getState():
    return GPIO.input(21)

def switchOn():
    if getState() == GPIO.LOW:
        toggle()

def switchOff():
    if getState() == GPIO.HIGH:
        toggle()

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(21, GPIO.IN)
    if len(sys.argv) < 2:
        cmd = 'status'
    else:
        cmd = sys.argv[1]
    if cmd == 'on':
        switchOn()
    elif cmd == 'off':
        switchOff()
    elif cmd == 'toggle':
        toggle()
    elif cmd == 'status':
        if getState() == GPIO.LOW:
            print('off')
        elif getState() == GPIO.HIGH:
            print('on')
    else:
        print('Unknown command.')

if __name__ == '__main__':
    main()
