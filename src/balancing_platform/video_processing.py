#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Object tracking based on HSV-mask.

Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/
"""

# Importing packages
import cv2
import numpy as np


class VideoProcessing(object):

    def __init__(self, capture, watch):
        self.DEBUG = watch
        self.x = 0
        self.y = 0
        self.cap = capture

    def getCoordinates(self):
        _, frame = self.cap.read()

        # Convert RGB to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Defining the color  in HSV
        # Find limits using morphological_transformation.py
        lower_color = np.array([0, 58, 119])
        upper_color = np.array([95, 187, 210])

        # Creates a mask
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Enlarge the mask
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(mask, kernel)

        # Finding the contours
        im2, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Mark up only the largest contour
        if len(contours) > 0:
            ball = max(contours, key=cv2.contourArea)
            cv2.drawContours(frame, ball, -1, (0, 255, 0), 3)
            M = cv2.moments(ball)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            self.x = center[0]
            self.y = center[1]
            if self.DEBUG:
                self.watch(frame, dilation)
            return center
        else:
            if self.DEBUG:
                self.watch(frame, dilation)
            return None

    def watch(self, frame, dilation):
        # Show frame with contour and mask
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", dilation)

    def stop(self):
        # Close all windows
        self.cap.release()
        cv2.destroyAllWindows()
        return True


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    vp = VideoProcessing(cap, watch=True)

    while True:
        coordinates = vp.getCoordinates()
        print(coordinates)
        # Break loop with ESC-key
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break
            running = vp.stop()
