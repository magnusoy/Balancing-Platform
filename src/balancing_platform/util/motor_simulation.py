#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Code by: Magnus Øye, Dated: 20.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
import numpy as np
from math import sqrt, acos, pi
import matplotlib.pyplot as plt


xValue = 0
yValue = 0
zValue = 0

length = 45.0
Z0 = 9.0
offset = 4.0
radius = 9.0
countsPerRev = 400000
angles = np.linspace(-10.0, 10.0, num=50)

X = []
Y1 = []
Y2 = []
Y3 = []

for xValue in angles:
    print('#'*50)
    roll = xValue * (pi/180.0)
    pitch = yValue * (pi/180.0)
    print('Roll: ', roll)
    print('Pitch: ', pitch)

    heightM1 = (sqrt(3)/3) * length * pitch + Z0
    heightM2 = -(sqrt(3)/6) * length * pitch + (length / 2) * roll + Z0
    heightM3 = -(sqrt(3)/6) * length * pitch - (length / 2) * roll + Z0
    print('Height: ', heightM1, heightM2, heightM3)

    angleM1 = acos(((heightM1 * heightM1) + (offset * offset) - (radius * radius)) / (2.0 * offset * heightM1))
    angleM2 = acos(((heightM2 * heightM2) + (offset * offset) - (radius * radius)) / (2.0 * offset * heightM2))
    angleM3 = acos(((heightM3 * heightM3) + (offset * offset) - (radius * radius)) / (2.0 * offset * heightM3))

    degreeM1 = (angleM1*180.0)/pi
    degreeM2 = (angleM2*180.0)/pi
    degreeM3 = (angleM3*180.0)/pi
    print('Degrees: ', degreeM1, degreeM2, degreeM3)

    outM1 = angleM1 * (countsPerRev / 2 * pi)
    outM2 = angleM2 * (countsPerRev / 2 * pi)
    outM3 = angleM3 * (countsPerRev / 2 * pi)
    print('Counts: ', outM1, outM2, outM3)
    X.append(xValue)
    Y1.append(outM1)
    Y2.append(outM2)
    Y3.append(outM3)

plt.plot(X, Y1)
plt.plot(X, Y2)
plt.plot(X, Y3)

plt.show()