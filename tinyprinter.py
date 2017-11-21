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

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(21, GPIO.IN)

def main():
    init()
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
        print("Content-type: text/html")
        print("")
        print("<html><head><title>Druckerstatus</title></head><body>")
        if getState() == GPIO.LOW:
            state = "aus"
        elif getState() == GPIO.HIGH:
            state = "an"
        print("<p>Drucker ist " + state + ".</p>")
        print("</body></html>")
    else:
        print('Unknown command.')

if __name__ == '__main__':
    main()
