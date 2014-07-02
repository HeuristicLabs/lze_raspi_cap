import time
import picamera

#camera = picamera.PiCamera()
#try:
#	camera.start_preview()
#	time.sleep(10)
#	camera.stop_preview()
#finally:
#	camera.close()

with picamera.PiCamera() as camera:
	camera.resolution = (1280,720)
	camera.start_preview()
	#camera.exposure_compensation = 2
	#camera.exposure_mode = 'spotlight'
	#camera.meter_mode = 'matrix'
	#camera.image_effect = 'gpen'
	time.sleep(2) # give camera time to adjust params
	t0 = time.time()
	camera.capture_sequence( ( '/tmp/image%03d.jpg' % i for i in range(120) ), use_video_port=True)
	print 'Captured 120 images at %.2ffps' % (120/(time.time()-t0))	
#	for i, filename in enumerate(camera.capture_continuous('/tmp/image{counter:02d}.jpg')):
#		print('Captured image %s' % filename)
#		if i >= 100:
#			break
#		time.sleep(0.1)
	camera.stop_preview()

