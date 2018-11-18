#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Code by: Magnus Øye, Dated: 12.11-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
import numpy as np
from numpy import sqrt, sin, cos, pi, arccos
import matplotlib.pylab as plt

# Plot style
plt.style.use("bmh")

# Constants
L = 45  # Length of one side
Z0 = 8.0  # Start lifting height
A = 4.0  # Center offset
r = 9.0  # Radius
countsPerRev = 400000  # Motor counts per revolution
pitch = 0  # Movement in Y-axis
roll = 0  # Movement in X-axis
anglesPitch = np.linspace(-0.139626, 0.139626, num=50)  # Array of linearly spaced angels from -8, 8 degrees
anglesRoll = np.linspace(-0.139626, 0.139626, num=50)  # Array of linearly spaced angels from -8, 8 degrees

# Lists for holding simulation data
X = []
Y1 = []
Y2 = []
Y3 = []

# Simulating platform movements
for angle in anglesPitch:
    deg = angle * 180 / pi
    pitch = angle
    roll = 0

    # Motor lift height
    z1 = ((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) + ((L/2)*sin(roll)) + Z0
    z2 = ((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) - ((L/2)*sin(roll)) + Z0
    z3 = -((sqrt(3) * L) / 3) * sin(pitch) * cos(roll) + Z0

    # Motor angles in radians
    angleM1 = arccos(((z1**2) + (A**2) - (r**2)) / (2.0 * A * z1))
    angleM2 = arccos(((z2**2) + (A**2) - (r**2)) / (2.0 * A * z2))
    angleM3 = arccos(((z3**2) + (A**2) - (r**2)) / (2.0 * A * z3))

    # Motor angles in degrees
    degreeM1 = (angleM1 * 180.0) / pi
    degreeM2 = (angleM2 * 180.0) / pi
    degreeM3 = (angleM3 * 180.0) / pi

    # Motor position in counts
    outM1 = angleM1 * (countsPerRev / 2 * pi)
    outM2 = angleM2 * (countsPerRev / 2 * pi)
    outM3 = angleM3 * (countsPerRev / 2 * pi)

    # Adding values in array for visual representation
    X.append(deg)
    Y1.append(z1)
    Y2.append(z2)
    Y3.append(z3)

# Plotting values

fig, axes = plt.subplots(1, 3, constrained_layout=True)
fig.suptitle('Pitch +/- 8 grader | Roll +/- 0 grader', size=16)
ax_m1 = axes[0]
ax_m2 = axes[1]
ax_m3 = axes[2]
ax_m1.set_title('Motor 1 løftehøyde')
ax_m2.set_title('Motor 2 løftehøyde')
ax_m3.set_title('Motor 3 løftehøyde')
ax_m1.set_xlabel('Rotasjon [Grader]')
ax_m2.set_xlabel('Rotasjon [Grader]')
ax_m3.set_xlabel('Rotasjon [Grader]')
ax_m1.set_ylabel('Høyde [cm]')
ax_m2.set_ylabel('Høyde [cm]')
ax_m3.set_ylabel('Høyde [cm]')
ax_m1.set_xlim(-8, 8)
ax_m2.set_xlim(-8, 8)
ax_m3.set_xlim(-8, 8)
ax_m1.set_ylim(0, 15)
ax_m2.set_ylim(0, 15)
ax_m3.set_ylim(0, 15)

ax_m1.plot(X, Y1, label='M1')
ax_m2.plot(X, Y2, label='M2')
ax_m3.plot(X, Y3, label='M3')
ax_m1.legend()
ax_m2.legend()
ax_m3.legend()

# Showing values
plt.show()
