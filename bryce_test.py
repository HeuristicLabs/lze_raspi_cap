#!/usr/bin/python

# if RPi.GPIO is not installed, get it via http://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/

import RPi.GPIO as GPIO
import time
import picamera
import datetime  # new

def getFileName():  # new
    return 'test.h264'
    #return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

def getImageFileName():  # new
    #return 'test.h264'
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

flashPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(flashPin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

prevState = True # NAC: testing ; remove for real use
currState = True # NAC: testing ; remove for real use
#prevState = False
#currState = False

cam = picamera.PiCamera()

showGUI = False # better for remote triggering or headless RPi
#showGUI = True

while True:
    time.sleep(5.0)
    print 'tick'
    prevState = currState
    prevState = not currState # NAC: testing ; remove for real use
    currState = GPIO.input(flashPin)
    if currState != prevState:
        newState = "HIGH" if currState else "LOW"
        print "GPIO pin %s is %s" % (flashPin, newState)
        #if currState:
        if True: #currState:
            #fileName = getFileName()  # new
            fileName = getImageFileName()  # new
            if showGUI:
            	cam.start_preview()
            print "Recording to %s!" % fileName
            #cam.start_recording(fileName)  # new
            print 'tick: %s' % datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
            cam.capture(fileName)
            print 'tock: %s' % datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        else:
            if showGUI:
            	cam.stop_preview()
            #cam.stop_recording()  # new
            print 'Stopped recording.'


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
