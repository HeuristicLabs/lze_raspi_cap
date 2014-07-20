#!/usr/bin/env python

import time
import picamera

import socket
import sys
import time
import struct
import numpy as np

import RPi.GPIO as GPIO

#import datetime  # new

#def getFileName():  # new
#    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

dt = 0.02 # 50 hz

flashPin = 7 # GPIO pin

#UDP_HOST_OUT = 'localhost'
UDP_HOST_OUT = '127.0.0.1'
UDP_PORT_OUT = 6000

# set up network stuff
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
out_addr = (UDP_HOST_OUT,UDP_PORT_OUT)

# set up GPIO stuff
GPIO.setmode(GPIO.BOARD)
GPIO.setup(flashPin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

with picamera.PiCamera() as camera:
	# setup camera
	camera.resolution = (640,480)
	camera.framerate = 90
	camera.start_preview()
	#camera.exposure_compensation = 2
	#camera.exposure_mode = 'spotlight'
	#camera.meter_mode = 'matrix'
	#camera.image_effect = 'gpen'
	time.sleep(2) # give camera time to adjust params

	#t0 = time.time()
	#camera.capture_sequence( ( '/tmp/image%03d.jpg' % i for i in range(120) ), use_video_port=True)
	#print 'Captured 120 images at %.2ffps' % (120/(time.time()-t0))	

	for i, filename in enumerate(camera.capture_continuous('/tmp/image{counter:03d}.jpg')):

		# GPIO flash sync
		laserOn = GPIO.input(flashPin)
		print "Got GPIO pin %s as %s" % (flashPin, laserOn)
		newState = "HIGH" if bool(i%2) else "LOW"
		GPIO.output(flashPin, bool(i%2)) # every other frame, turn on laser
		print "Set GPIO pin %s to %s" % (flashPin, newState)

		# send network sync signal
		#data = struct.pack('!hhhhhh', np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand())
		data = struct.pack('!B', i%2) # send count (as single byte)
		sent = sock.sendto(data, out_addr)
		print >>sys.stderr, 'sent %s bytes to %s' % (sent, out_addr)

		print 'Captured image %s' % filename
		if i >= 100:
			break

		time.sleep(dt)

	camera.stop_preview()



# see http://blog.derivatived.com/posts/OpenCV-Tutorial-on-Face-Tracking-Raspberry-PI-Camera/
#import io
##saving the picture to an in-program stream rather than a file
#stream = io.BytesIO()
#camera.capture(stream, format='jpeg')
##convert image into numpy array
#data = np.fromstring(stream.getvalue(), dtype=np.uint8)
##turn the array into a cv2 image
#image = cv2.imdecode(data, 1)
## now do stuff w/ opencv ... like average image frames to remove noise, background subtraction, or select every-other-frame to get signal

# for HW modding (e.g., lenses), see http://wiki.raspberrytorte.com/index.php?title=Camera_Module_Lens_Modifcation
# and https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/assembling-enclosure


