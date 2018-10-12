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
from modbus_communication import ModbusClient

if __name__ == '__main__':
    running = True
    cap = cv2.VideoCapture(0)
    client = ModbusClient()

    vp = VideoProcessing(cap, watch=True)

    while client.isConnected():
        coordinates = vp.getCoordinates()
        client.send(coordinates[0])
        client.send(coordinates[1])

        # Break loop with ESC-key
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            vp.stop()
            break
