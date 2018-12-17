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


def constrain(x, lower, upper):
    y = 0
    if x > upper:
        y = upper
    elif x < lower:
        y = lower
    if x > 6500:
        y = 0
    else:
        y = x
    return y


# Platform Constants
L = 45  # Length of one side
Z0 = 8.0  # Start lifting height
A = 4.0  # Center offset
r = 9.0  # Radius'

# Variables
pitch, roll = 0.0, 0.0
x_pos, y_pos = 0, 0
t = 0.0

# Modbus addresses
addresses = {
    'Ball X': 9,  # Position in array
    'Ball Y': 11,  # Position in array
    'Pitch': 12301,  # Position in Modbus
    'Roll': 12303,  # Position in Modbus
    'Setpoint X': 17,  # Position in array
    'Setpoint Y': 19  # Position in array
}

# Creating visualization scene
scene.title = "Balancing Platform Visualization"
scene.x = 0
scene.y = 0
scene.width = 1280
scene.height = 720
scene.range = 30
scene.center = vector(1, 0, 0)
scene.background = vector(0, 0, 0)

# Creating objects
set_ball = sphere(pos=vector(0, 1, 0), radius=0.5, color=color.red)
ball = sphere(pos=vector(0, 1, 0), radius=0.5, color=color.blue)
platform = box(length=50, height=1.0, width=50, color=color.orange)
floor = box(pos=vector(0, -8.75, 0), size=vector(100, 1, 100), color=color.white)
leg_1 = cylinder(pos=vector(20, -Z0 - 0.4, 20), axis=vector(0, 8.75, 0), radius=1, color=color.green)
leg_2 = cylinder(pos=vector(-20, -Z0 - 0.4, 20), axis=vector(0, 8.75, 0), radius=1, color=color.green)
leg_3 = cylinder(pos=vector(0, -Z0 - 0.4, -20), axis=vector(0, 8.75, 0), radius=1, color=color.green)
x_graph = graph(title="Ballmovement in X direction", xtitle='Time[s]', ytitle='X[%]',
                fast=False, width=800, ymin=0, ymax=100, x=0, y=0)
x_position = gcurve(color=color.blue)
set_x_position = gcurve(color=color.red)
y_graph = graph(title="Ballmovement in Y direction", xtitle='Time[s]', ytitle='Y[%]',
                fast=False, width=800, ymin=0, ymax=100, x=300, y=300)
y_position = gcurve(color=color.blue)
set_y_position = gcurve(color=color.red)
platform.pos = vector(0, 0, 0)

# Create modbus client
client = ModbusClient()

# Running visualization
while client.isConnected():
    # Refresh rate
    rate(10)
    t += 0.1

    # Read modbus addresses for data
    response = client.readInt(address=12288, size=20)
    x_pos = response[addresses['Ball X']]
    y_pos = response[addresses['Ball Y']]
    set_x_pos = response[addresses['Setpoint X']]
    set_y_pos = response[addresses['Setpoint Y']]
    roll = client.readFloat(address=addresses['Pitch'], size=2)
    pitch = client.readFloat(address=addresses['Roll'], size=2)

    # Convert to radians
    pitch = translate(pitch, 0, 100, -8, 8)
    roll = translate(roll, 0, 100, -8, 8)
    pitch = pitch * pi / 180
    roll = roll * pi / 180

    # Graphing values
    x_position.plot((t, constrain(x_pos, 0, 100)))
    set_x_position.plot((t, set_x_pos))
    y_position.plot((t, y_pos))
    set_y_position.plot((t, set_y_pos))

    # Map in values to range that fits platform
    x_pos = translate(x_pos, 1, 100, -25, 25)
    y_pos = translate(y_pos, 1, 100, -25, 25)
    set_x_pos = translate(set_x_pos, 1, 100, -25, 25)
    set_y_pos = translate(set_y_pos, 1, 100, -25, 25)

    # Calculate leg heights from transformation position matrix
    y1 = -((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) + ((L / 2) * sin(roll)) + Z0
    y2 = -((sqrt(3) * L) / 6) * sin(pitch) * cos(roll) - ((L / 2) * sin(roll)) + Z0
    y3 = ((sqrt(3) * L) / 3) * sin(pitch) * cos(roll) + Z0

    # Assign data to visualization objects
    platform.up = vector(sin(roll), 1, sin(pitch))
    leg_1.axis = vector(0, y2, 0)
    leg_2.axis = vector(0, y1, 0)
    leg_3.axis = vector(0, y3, 0)

    # Update ball position
    if x_pos == -25 and y_pos == -25:
        ball.visible = False
    else:
        ball.visible = True
        ball.pos = vector(x_pos, 1 + x_pos * sin(-roll) + y_pos * sin(-pitch), y_pos)

    set_ball.pos = vector(set_x_pos, 1 + set_x_pos * sin(-roll) + set_y_pos * sin(-pitch), set_y_pos)
