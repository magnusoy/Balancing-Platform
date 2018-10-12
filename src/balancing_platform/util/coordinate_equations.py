#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulate gyroscope degrees of freedom, and
watch ball roll around platform accordingly.

Code by: Magnus Øye, Dated: 06.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/
"""

# Importing packages
import numpy as np
import matplotlib.pylab as plt

plt.style.use("ggplot")


def plot_motor_lift():
    """docstring"""
    x_rad = np.linspace(0.01, 2 * np.pi, num=100)
    x_degrees = np.degrees(x_rad)
    pulses = 8000 / 360
    x_pulses = x_rad * pulses
    y = 8.75 + 4.5 * np.sin(x_rad)
    fig, axs = plt.subplots(1, 3)
    ax_rad = axs[0]
    ax_rad.set_title("Motor lift in radians")
    ax_rad.set_xlabel('Rotation [rad]')
    ax_rad.set_ylabel('Height [cm]')
    ax_rad.set_xlim(0, 2 * np.pi)
    ax_rad.set_ylim(0, 15)
    ax_rad.plot(x_rad, y)

    ax_degrees = axs[1]
    ax_degrees.set_title("Motor lift in degrees")
    ax_degrees.set_xlabel('Rotation [degrees]')
    ax_degrees.set_xlim(0, 360)
    ax_degrees.set_ylim(0, 15)
    ax_degrees.plot(x_degrees, y)

    ax_pulses = axs[2]
    ax_pulses.set_title("Motor lift in pulses")
    ax_pulses.set_xlabel('Rotation [pulses]')
    ax_pulses.set_xlim(0, 140)
    ax_pulses.set_ylim(0, 15)
    ax_pulses.plot(x_pulses, y)
    plt.show()


plot_motor_lift()
