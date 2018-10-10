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

# Giving location to find textures
floor_texture = "\\floor_texture.jpg"
platform_texture = "\\platform_texture.jpg"
ball_texture = "\\ball_texture.jpg"
wall_texture = "\\wall_texture.jpg"

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
ball = sphere(pos=vector(0, 0.745, 0), radius=0.5,  make_trail=True)
platform = box(pos=vector(0, 0, 0), size=vector(50, 0.5, 50))
floor = box(pos=vector(0, -8.75, 0), size=vector(100, 1, 100))
wall_1 = box(pos=vector(50, 40, 0), size=vector(5, 100, 100))
wall_2 = box(pos=vector(-50, 40, 0), size=vector(5, 100, 100))
wall_3 = box(pos=vector(0, 40, -50), size=vector(100, 100, 5))
leg_1 = cylinder(pos=vector(20, -8.75, 20), axis=vector(0, 8.75, 0), radius=1)
leg_2 = cylinder(pos=vector(-20, -8.75, 20), axis=vector(0, 8.75, 0), radius=1)
leg_3 = cylinder(pos=vector(0, -8.75, -20), axis=vector(0, 8.75, 0), radius=1)


def setpoint_x(s):
    wt_x.text = '{:1.2f}'.format(s.value)


def setpoint_z(s):
    wt_z.text = '{:1.2f}'.format(s.value)


# Sliders
sl_x = slider(min=-25, max=25, value=0, length=200, bind=setpoint_x, right=15)
wt_x = wtext(text='{:1.2f}'.format(sl_x.value))
sl_z = slider(min=-25, max=25, value=0, length=200, bind=setpoint_z, right=15)
wt_z = wtext(text='{:1.2f}'.format(sl_z.value))

# Assigning objects textures
platform.texture = {'file': platform_texture, 'bumpmap': None}
floor.texture = {'file': floor_texture, 'bumpmap': None}
ball.texture = {'file': ball_texture, 'bumpmap': None}
wall_1.texture = {'file': wall_texture, 'bumpmap': None}
wall_2.texture = {'file': wall_texture, 'bumpmap': None}
wall_3.texture = {'file': wall_texture, 'bumpmap': None}
leg_1.texture = {'file': platform_texture, 'bumpmap': None}
leg_2.texture = {'file': platform_texture, 'bumpmap': None}
leg_3.texture = {'file': platform_texture, 'bumpmap': None}





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
    pid_x.setpoint = 2 + (50 * cos(t)) / (1 + sin(t) * sin(t))
    pid_z.setpoint = 1 + (50 * sin(t) * cos(t)) / (1 + sin(t) * sin(t))


dt = 0.01
t = 0

# Simulation
while True:
    rate(100)
    number_8()
    control_x = pid_x(ball.pos.x)
    control_z = pid_z(ball.pos.z)
    update_x(control_x, dt)
    update_z(control_z, dt)
    t += dt
