#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Object tracking based on a HSV-mask,
and will contour out the biggest object
and find its coordinates in the x and y plane.

Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/
"""

# Importing packages
import cv2
import numpy as np


class VideoProcessing(object):
    """Finds biggest object according to HSV filtering.
    Returns the coordinates in x and y plane."""
    def __init__(self, capture, watch):
        self.DEBUG = watch
        self.cap = capture

    def getCoordinates(self):
        """Finds the biggest object.
        Return: X and Y coordinates from center of the object"""
        _, frame = self.cap.read()

        # Convert RGB to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Defining the color  in HSV
        # Find limits using morphological_transformation.py
        lower_color = np.array([29, 111, 187])
        upper_color = np.array([45, 163, 230])

        # Creates a mask
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Enlarge the mask
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(mask, kernel)

        # Finding the contours
        im2, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Mark up only the largest contour and draw centroid
        if len(contours) > 0:
            ball = max(contours, key=cv2.contourArea)
            cv2.drawContours(frame, ball, -1, (0, 255, 0), 3)
            M = cv2.moments(ball)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if self.DEBUG:
                cv2.circle(frame, center, 3, (0, 0, 255), -1)
                cv2.putText(frame, "centroid", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255),
                            1)
                cv2.putText(frame, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
                self.watch(frame, dilation)
            return center
        else:
            if self.DEBUG:
                self.watch(frame, dilation)
            return 0, 0

    @staticmethod
    def watch(frame, dilation):
        """Works as a debug functionality if user
        wants to see the frame and mask."""
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", dilation)

    def stop(self):
        """Releases the capture and close all frames runnning.
        Return: True when everything is closed."""
        self.cap.release()
        cv2.destroyAllWindows()
        return True


# Simple example of usage.
if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    cap.set(propId=3, value=640)
    cap.set(propId=4, value=480)
    vp = VideoProcessing(cap, watch=True)

    while True:
        coordinates = vp.getCoordinates()
        print(coordinates)
        # Break loop with ESC-key
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            running = vp.stop()
            break
