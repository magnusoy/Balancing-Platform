#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Object Tracking Test

Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
import cv2
from src.balancing_platform.video_processing import BallTracking

# Run test
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    ballTracking = BallTracking(cap, watch=True, color='red')
    tracking = True

    while tracking:
        coordinates = ballTracking.getCoordinates()
        print(coordinates)

        # Break loop with ESC-key
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            tracking = ballTracking.stop()
            break
