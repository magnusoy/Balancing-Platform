#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Code by: Magnus Øye, Dated: 02.11-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
import numpy as np
from numpy import sqrt, sin, cos, arccos, pi
import matplotlib.pyplot as plt

# Plot style
plt.style.use("bmh")

# Constants
L = 45  # Length of one side
Z0 = 9.0  # Start lifting height
A = 4.0  # Center offset
r = 9.0  # Radius
countsPerRev = 400000  # Motor counts per revolution
pitch = 0  # Movement in Y-axis
roll = 0  # Movement in X-axis
anglesPitch = np.linspace(-0.139626, 0.139626, num=50)  # Array of linearly spaced angels from 0, 8 degrees
anglesRoll = np.linspace(-0.139626, 0.139626, num=50)  # Array of linearly spaced angels from -8, 8 degrees

# Lists for holding simulation data
X = []
Y1 = []
Y2 = []
Y3 = []

# Position matrix
p1 = np.matrix([0, (sqrt(3) * L) / 3, 0])
p2 = np.matrix([L / 2, -((sqrt(3) * L) / 3), 0])
p3 = np.matrix([-L / 2, -((sqrt(3) * L) / 3), 0])

# Zero point matrix
p0 = np.matrix([[0, L / 2, -L / 2],
                [(sqrt(3) * L) / 3, -(sqrt(3) * L) / 3, -(sqrt(3) * L) / 3],
                [0, 0, 0]])

# Movement matrix
positionMatrix = np.array([[((sqrt(3) * L) / 6) * sin(pitch) * sin(roll),
                            (L / 2 * cos(roll)) - ((sqrt(3) * L) / 6) * sin(pitch) * sin(roll),
                            -(L / 2 * cos(roll)) - ((sqrt(3) * L) / 6) * sin(pitch) * sin(roll)],
                           [-((sqrt(3) * L) / 6) * cos(pitch), -((sqrt(3) * L) / 6) * cos(pitch),
                            ((sqrt(3) * L) / 6) * cos(pitch)],
                           [-((sqrt(3) * L) / 3) * sin(pitch) * cos(roll) + Z0,
                            (L / 2 * sin(roll)) + ((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) + Z0,
                            (-L / 2 * sin(roll)) + ((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) + Z0]])

# Simulating platform movements
for angle in anglesPitch:
    deg = angle * 180 / pi
    pitch = angle
    roll = 0
    print('#' * 50)
    print('Platform angle: ', deg)

    # Motor lift height
    z1 = ((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) + ((L/2)*sin(roll)) + Z0
    z2 = ((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) - ((L/2)*sin(roll)) + Z0
    z3 = -((sqrt(3) * L) / 3) * sin(pitch) * cos(roll) + Z0
    print('Height: ', z1, z2, z3)

    # Motor angles in radians
    angleM1 = arccos(((z1**2) + (A**2) - (r**2)) / (2.0 * A * z1))
    angleM2 = arccos(((z2**2) + (A**2) - (r**2)) / (2.0 * A * z2))
    angleM3 = arccos(((z3**2) + (A**2) - (r**2)) / (2.0 * A * z3))

    # Motor angles in degrees
    degreeM1 = (angleM1 * 180.0) / pi
    degreeM2 = (angleM2 * 180.0) / pi
    degreeM3 = (angleM3 * 180.0) / pi
    print('Degrees: ', degreeM1, degreeM2, degreeM3)

    # Motor position in counts
    outM1 = angleM1 * (countsPerRev / 2 * pi)
    outM2 = angleM2 * (countsPerRev / 2 * pi)
    outM3 = angleM3 * (countsPerRev / 2 * pi)
    print('Counts: ', outM1, outM2, outM3)

    # Adding values in array for visual representation
    X.append(deg)
    Y1.append(z1)
    Y2.append(z2)
    Y3.append(z3)

# Plotting values
plt.title('Simulation -8 to 8 degrees')
plt.plot(X, Y1, label='M1')
plt.plot(X, Y2, label='M2')
plt.plot(X, Y3, label='M3')
plt.legend()

# Showing values
plt.show()
