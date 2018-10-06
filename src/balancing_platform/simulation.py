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

# Giving location to find textures
floor_texture = "\\floor_texture.jpg"
platform_texture = "\\platform_texture.jpg"
ball_texture = "\\ball_texture.jpg"
wall_texture = "\\wall_texture.jpg"

# Creating simulation scene
scene.title = "Balancing Platform Simulation"
scene.x = 0
scene.y = 0
scene.width = 800
scene.height = 600
scene.range = 30
scene.center = vector(1, 0, 0)
scene.background = vector(0, 0, 0)

# Creating objects
ball = sphere(pos=vector(0, 0.745, 0), radius=0.5)
platform = box(pos=vector(0, 0, 0), size=vector(50, 0.5, 50))
floor = box(pos=vector(0, -10, 0), size=vector(100, 1, 100))
wall_1 = box(pos=vector(50, 40, 0), size=vector(5, 100, 100))
wall_2 = box(pos=vector(-50, 40, 0), size=vector(5, 100, 100))
wall_3 = box(pos=vector(0, 40, -50), size=vector(100, 100, 5))
leg_1 = box(pos=vector(20, -5, 20), size=vector(2.5, 10, 2.5))
leg_2 = box(pos=vector(-20, -5, 20), size=vector(2.5, 10, 2.5))
leg_3 = box(pos=vector(0, -5, -20), size=vector(2.5, 10, 2.5))

# Assigning objects textures
floor.texture = {'file': floor_texture, 'bumpmap': None}
wall_1.texture = {'file': wall_texture, 'bumpmap': None}
wall_2.texture = {'file': wall_texture, 'bumpmap': None}
wall_3.texture = {'file': wall_texture, 'bumpmap': None}
ball.texture = {'file': ball_texture, 'bumpmap': None}
platform.texture = {'file': platform_texture, 'bumpmap': None}
leg_1.texture = {'file': platform_texture, 'bumpmap': None}
leg_2.texture = {'file': platform_texture, 'bumpmap': None}
leg_3.texture = {'file': platform_texture, 'bumpmap': None}

dt = 0.1
ball.velocity = vector(1, 0, 1)
t = 0

# Simulation
while True:
    rate(100)
    ball.pos.x += ball.velocity.x * dt * 5*cos(t)
    ball.pos.z += ball.velocity.z * dt * 5*sin(t)
    if ball.pos.x > 25 or ball.pos.x < -25:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.z > 25 or ball.pos.z < -25:
        ball.velocity.z = -ball.velocity.z
    t += dt
