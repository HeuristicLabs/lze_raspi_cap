#!/bin/sh

raspistill --quality 75 --nopreview --verbose \
--width 1280 --height 720 \
--timeout 5000 --timelapse 20 \
--output /tmp/image%06d.jpg

# exposure sports --shutter 1000000

gpicview /tmp/*.jpg
