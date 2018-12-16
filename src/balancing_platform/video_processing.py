#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Object tracking based on a HSV-mask,
and will contour out the biggest object
and find its coordinates in the x and y plane.

Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
import cv2
import numpy as np


class BallTracking(object):
    """Finds biggest object according to HSV filtering.
    Returns the coordinates in x and y plane."""
    def __init__(self, capture, watch, color='green'):
        self.frame = watch
        self.cap = capture
        self.lower_color = np.array([29, 125, 85])
        self.upper_color = np.array([39, 181, 182])
        self.setColor(color)

    def setColor(self, color):
        """Defining the color  in HSV.
        Find limits using morphological_transformation.py"""
        if color == "green":
            self.lower_color = np.array([29, 125, 85])
            self.upper_color = np.array([39, 181, 182])
        elif color == "red":
            self.lower_color = np.array([0, 255, 140])
            self.upper_color = np.array([24, 255, 255])

    def getCoordinates(self):
        """Finds the biggest object.
        Return: X and Y coordinates from center of the object"""
        _, frame = self.cap.read()

        # Convert RGB to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Scale down frame to fit platform dimension
        roi = frame[0: 480, 60: 570]
        frame = cv2.bitwise_and(roi, roi)

        # Creates a mask
        mask = cv2.inRange(hsv, self.lower_color, self.upper_color)

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
            if self.frame:
                cv2.circle(frame, center, 3, (0, 0, 255), -1)
                cv2.putText(frame, "centroid", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255),
                            1)
                cv2.putText(frame, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
                self.watch(frame, dilation)
            return center
        else:
            if self.frame:
                self.watch(frame, dilation)
            return 0, 0

    @staticmethod
    def watch(frame, dilation):
        """Works as a debug functionality if user
        wants to see the frame and mask."""
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", dilation)

    def stop(self):
        """Releases the capture and close all frames running.
        Return: True when everything is closed."""
        self.cap.release()
        cv2.destroyAllWindows()
        return True


# Simple example of usage.
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    ballTracking = BallTracking(cap, watch=True, color='red')

    while True:
        coordinates = ballTracking.getCoordinates()
        print(coordinates)
        # Break loop with ESC-key
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            ballTracking.stop()
            break
