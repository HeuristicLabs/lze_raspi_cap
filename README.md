lze_raspi_cap
=============

Install notes

1) install raspbian jessie image
2) rpi-update to get latest firmware (see https://github.com/Hexxeh/rpi-update , Readme.md, use curl method)
3) load picam firmware: mike632t.wordpress.com/2014/06/26/raspberry-pi-camera-setup/#more-1843
4) get repo from: `ssh-add ~/.ssh/id_rsa && git clone git@github.com:HeuristicLabs/lze_raspi_cap.git`
5) now, picamera_test.py and picamera_test.sh should work and when run will put test images in /tmp/image*.jpg
6) modify/customize using docs at picamera.readthedocs.org
