#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Draw on canvas and extracts the coordinates
from each of the drawn rectangles.

Code by: Magnus Øye, Dated: 29.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
import cv2
import numpy as np

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve


# mouse callback function
def interactive_drawing(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
                print(x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.circle(img, (x, y), 1, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Window')
cv2.setMouseCallback('Window', interactive_drawing)
while True:
    cv2.imshow('Window', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
