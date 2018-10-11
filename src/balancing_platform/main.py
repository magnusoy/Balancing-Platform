#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/
"""

# Importing packages
import cv2
from video_processing import VideoProcessing
from modbus_communication import Communication

if __name__ == '__main__':
    running = True
    cap = cv2.VideoCapture(0)
    vp = VideoProcessing(cap, watch=True)

    while running:
        coordinates = vp.getCoordinates()
        print(coordinates)
        # Break loop with ESC-key
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            running = vp.stop()
