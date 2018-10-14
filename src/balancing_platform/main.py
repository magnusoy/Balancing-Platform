#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Locates ball on platform and sends the
X and Y coordinates over Modbus to assigned
slave on ip: 192.168.2.17, port: 502.

Code by: Magnus Øye, Dated: 13.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/
"""

# Importing packages
import cv2
from video_processing import VideoProcessing
from modbus_communication import ModbusClient

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    client = ModbusClient()

    vp = VideoProcessing(cap, watch=True)

    while client.isConnected():
        coordinates = vp.getCoordinates()
        client.send(value=coordinates[0], address=12288)
        client.send(value=coordinates[1], address=12290)

        # Break loop with ESC-key
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            vp.stop()
            break
