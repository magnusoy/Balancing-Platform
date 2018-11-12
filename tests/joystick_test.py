#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Joystick Control Test

Code by: Magnus Øye, Dated: 23.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing package
from src.balancing_platform.joystick import Joystick

if __name__ == '__main__':
    joystick = Joystick()

    while True:
        values = joystick.getEvents()
        print(values)
