#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reads the different axis and button presses
from serial and returns them for further usage.

Code by: Magnus Øye, Dated: 23.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing package
import pygame


class Joystick(object):

    pygame.init()
    pygame.joystick.init()

    def __init__(self):
        self.lastMove0 = 0
        self.lastMove1 = 0
        self.rounded1 = 0
        self.rounded2 = 0
        try:
            self.joystick = pygame.joystick.Joystick(0)  # create a joystick instance
            self.joystick.init()  # init instance
            print(f'Enabled joystick: {self.joystick.get_name()}')
        except pygame.error:
            print('No joystick found.')

    def getEvents(self):
        """docstring"""
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:  # Joystick
                if self.joystick.get_axis(0) != self.lastMove0 or self.joystick.get_axis(1) != self.lastMove1:
                    self.lastMove0 = self.joystick.get_axis(0)
                    self.lastMove1 = self.joystick.get_axis(1)
                    self.rounded1 = round(self.joystick.get_axis(0), 3)
                    self.rounded2 = round(self.joystick.get_axis(1), 3)
                    # print(f'Axis 0: {rounded1}  |  Axis 1: {rounded2}')

            if event.type == pygame.JOYBUTTONDOWN:
                pass
                # print("Joystick Button pressed")
        return self.rounded1, self.rounded2


# Simple example of usage
if __name__ == '__main__':
    joystick = Joystick()

    while True:
        coord = joystick.getEvents()
        print(coord)
