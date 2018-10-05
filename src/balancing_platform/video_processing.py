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

# Start recording on camera
cap = cv2.VideoCapture(0)

while True:
    # Take each frame
    _, frame = cap.read()

    # Convert RGB to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Defining the color  in HSV
    # Find limits using morphological_transformation.py
    lower_color = np.array([0, 64, 49])
    upper_color = np.array([116, 117, 155])

    # Creates a mask
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Enlarge the mask
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(mask, kernel)

    # Finding the contours
    im2, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Mark up only the largest contour
    ball = max(contours, key=cv2.contourArea)
    cv2.drawContours(frame, ball, -1, (0, 255, 0), 3)

    # ((x, y), radius) = cv2.minEnclosingCircle(ball)

    # Find movements and calculates the center of the object
    M = cv2.moments(ball)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    # Show frame with contour and mask
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", dilation)

    print(center)

    # Break loop with ESC-key
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

# Close all windows
cap.release()
cv2.destroyAllWindows()
