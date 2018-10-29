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
from vpython import *
import numpy as np
from simple_pid import PID

pid_x = PID(2, 0.1, 0.05, setpoint=0)
pid_z = PID(1, 0.1, 0.05, setpoint=0)

# Creating simulation scene
scene.title = "Balancing Platform Simulator"
scene.x = 0
scene.y = 0
scene.width = 800
scene.height = 600
scene.range = 30
scene.center = vector(1, 0, 0)
scene.background = vector(0, 0, 0)

# Creating objects
ball = sphere(pos=vector(0, 0.745, 0), radius=0.5,  make_trail=True, color=color.green)
platform = box(pos=vector(0, 0, 0), size=vector(50, 0.5, 50), color=color.red)
floor = box(pos=vector(0, -8.75, 0), size=vector(100, 1, 100), color=color.cyan)
wall_1 = box(pos=vector(50, 40, 0), size=vector(5, 100, 100), color=color.blue)
wall_2 = box(pos=vector(-50, 40, 0), size=vector(5, 100, 100), color=color.blue)
wall_3 = box(pos=vector(0, 40, -50), size=vector(100, 100, 5), color=color.blue)
leg_1 = cylinder(pos=vector(20, -8.75, 20), axis=vector(0, 4, 0), radius=1, color=color.green)
leg_2 = cylinder(pos=vector(-20, -8.75, 20), axis=vector(0, 8.75, 0), radius=1, color=color.green)
leg_3 = cylinder(pos=vector(0, -8.75, -20), axis=vector(0, 8.75, 0), radius=1, color=color.green)


def update_x(power, dt):
        ball.pos.x += 1 * power * dt


def update_z(power, dt):
        ball.pos.z += 1 * power * dt


def ellipse():
    pid_x.setpoint = 2 + 20 * cos(t)
    pid_z.setpoint = 1 + 12.5 * sin(t)


def circle():
    pid_x.setpoint = 2 + 25 * cos(t)
    pid_z.setpoint = 2 + 25 * sin(t)


def number_8():
    pid_x.setpoint = 2 + (25 * cos(t)) / (1 + sin(t) * sin(t))
    pid_z.setpoint = 1 + (25 * sin(t) * cos(t)) / (1 + sin(t) * sin(t))


dt = 0.01
t = 0

xValue = 0
yValue = 0
length = 45.0
Z0 = 9.0
offset = 4.0

'''
# Simulation
while True:
    rate(100)
    number_8()
    control_x = pid_x(ball.pos.x)
    control_z = pid_z(ball.pos.z)
    update_x(control_x, dt)
    update_z(control_z, dt)
    t += dt

'''
while True:
    rate(100)
    roll = xValue * (pi / 180.0)
    pitch = yValue * (pi / 180.0)

    heightM1 = (sqrt(3) / 3) * length * pitch + Z0
    heightM2 = -(sqrt(3) / 6) * length * pitch + (length / 2) * roll + Z0
    heightM3 = -(sqrt(3) / 6) * length * pitch - (length / 2) * roll + Z0
    print('Height: ', heightM1, heightM2, heightM3)
    leg_1.axis.y = heightM1
    leg_2.axis.y = heightM2
    leg_3.axis.y = heightM3
    yValue += dt
    xValue += dt
