#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Visualization of the ball and the
moving platform.

Code by: Magnus Øye, Dated: 06.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
from vpython import *
from modbus_communication import ModbusClient
from numpy import sqrt, sin, cos


def translate(x, lowerIn, upperIn, lowerOut, upperOut):
    """Map in value range to another range"""
    y = (x - lowerIn) / (upperIn - lowerIn) * (upperOut - lowerOut) + lowerOut
    return y


# Constants
L = 45  # Length of one side
Z0 = 9.0  # Start lifting height
A = 4.0  # Center offset
r = 9.0  # Radius'

# Variables
pitch = 0.0
roll = 0.0
x_pos = 0
y_pos = 0

# Creating simulation scene
scene.title = "Balancing Platform Visualization"
scene.x = 0
scene.y = 0
scene.width = 800
scene.height = 600
scene.range = 30
scene.center = vector(1, 0, 0)
scene.background = vector(0, 0, 0)

# Creating objects
ball = sphere(pos=vector(0, 1.2, 0), radius=0.5, make_trail=False, color=color.green)
platform = box(length=50, height=1.0, width=50, color=color.red)
floor = box(pos=vector(0, -8.75, 0), size=vector(100, 1, 100), color=color.cyan)
wall_1 = box(pos=vector(50, 40, 0), size=vector(5, 100, 100), color=color.blue)
wall_2 = box(pos=vector(-50, 40, 0), size=vector(5, 100, 100), color=color.blue)
wall_3 = box(pos=vector(0, 40, -50), size=vector(100, 100, 5), color=color.blue)
leg_1 = cylinder(pos=vector(20, -Z0, 20), axis=vector(0, 8.75, 0), radius=1, color=color.green)
leg_2 = cylinder(pos=vector(-20, -Z0, 20), axis=vector(0, 8.75, 0), radius=1, color=color.green)
leg_3 = cylinder(pos=vector(0, -Z0, -20), axis=vector(0, 8.75, 0), radius=1, color=color.green)
platform.pos = vector(0, 0, 0)

# Create modbus client
client = ModbusClient()

while client.isConnected():
    # Refresh rate
    rate(100)

    # Read modbus addresses for data
    x_pos = client.read(12996)
    y_pos = client.read(12998)
    x_pos = translate(x_pos, 0, 100, -25, 25)
    y_pos = translate(y_pos, 0, 100, -25, 25)

    # Calculate leg heights from transformation position matrix
    z1 = ((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) + ((L / 2) * sin(roll)) + Z0
    z2 = ((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) - ((L / 2) * sin(roll)) + Z0
    z3 = -((sqrt(3) * L) / 3) * sin(pitch) * cos(roll) + Z0

    # Assign data to visualization objects
    platform.up = vector(sin(roll), 1, sin(-pitch))
    leg_1.axis = vector(0, z2, 0)
    leg_2.axis = vector(0, z1, 0)
    leg_3.axis = vector(0, z3, 0)
    ball.pos = vector(x_pos, 1 + x_pos*sin(-roll) + y_pos*sin(pitch), y_pos)
