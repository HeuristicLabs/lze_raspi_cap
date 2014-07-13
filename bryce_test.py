#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import picamera
import datetime  # new

def getFileName():  # new
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

flashPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(flashPin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

cam = picamera.PiCamera()

while True:
    time.sleep(2.0)
    prevState = currState
    currState = GPIO.input(flashPin)
    if currState != prevState:
        newState = "HIGH" if currState else "LOW"
        print "GPIO pin %s is %s" % (flashPin, newState)
        if currState:
            fileName = getFileName()  # new
            cam.start_preview()
            cam.start_recording(fileName)  # new
        else:
            cam.stop_preview()
            cam.stop_recording()  # new


#Note that if you don't like the cam.start/stop you should be able to replace:

#if currState:
#            fileName = getFileName()  # new
#            cam.start_preview()
#            cam.start_recording(fileName)  # new
#        else:
#            cam.stop_preview()
#            cam.stop_recording()  # new
#
#with:
#raspistill -o test.jpg 
