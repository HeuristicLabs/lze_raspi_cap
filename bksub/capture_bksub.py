#!/usr/bin/env python

INTERLEAVED = True # else, first capture many imgs of one, then other, then subtract

# captures 2*num_images, where
#def capture(path, exposure_time, num_images, interleaved = true)
# for i=1:2*num_images
# patternOn = not patternOn if INTERLEAVED else i>num_images
# filename = %04d.png
## how to save PNG uncompressed?
## can we save this many in memory? if so, don't waste time writing to disk?
## if interleaved, can we do bksub operation while streaming?


import picamera
import time

with picamera.PiCamera() as camera:
	# setup camera
	camera.resolution = (640,480)
	camera.framerate = 90

	#camera.start_preview()
	# http://picamera.readthedocs.org/en/release-1.6/api.html#picamera.PiCamera.brightness
	# camera.awb_mode = 'off'
	# camera.awb_gains = (0,0) # (red,blue), range is [0,8]
	#camera.contrast # [-100,100]
	#camera.crop = (x, y, w, h) # range 0,1
	# camera.digital_gain 
	camera.ISO = 800 # [0,800], disables exposure mode
	camera.exposure_compensation = 10 # [-25,25]
	camera.exposure_mode = 'fixedfps' # {u'auto': 1, u'fireworks': 12, u'verylong': 9, u'fixedfps': 10, u'backlight': 4, u'antishake': 11, u'snow': 7, u'sports': 6, u'nightpreview': 3, u'night': 2, u'beach': 8, u'spotlight': 5}
	camera.meter_mode = 'backlit'
	# camera.saturation # [-100,100]
	# camera.sharpness # [-100,100]
	#camera.image_effect = 'gpen'
	camera.shutter_speed = 11111 # microseconds, must be > 1/fps
	time.sleep(2) # give camera time to adjust params

	t0 = time.time()
	camera.capture_sequence( ( '/tmp/image%03d.jpg' % i for i in range(120) ), use_video_port=True)
	print 'Captured 120 images at %.2ffps' % (120/(time.time()-t0))	
