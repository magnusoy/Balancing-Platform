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
    """Starts a Pygame instance for recording
     joystick events."""

    pygame.init()
    pygame.joystick.init()

    def __init__(self):
        self.x = 0
        self.y = 0
        try:
            self.joystick = pygame.joystick.Joystick(0)  # create a joystick instance
            self.joystick.init()  # init instance
            print(f'Enabled joystick: {self.joystick.get_name()}')
        except pygame.error:
            print('No joystick found.')

    def getEvents(self):
        """Records events from joystick.
        Returns X and Y values in range from -1 to 1"""
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:  # Joystick
                if self.joystick.get_axis(0) > 0.10:
                    self.x = -1
                elif self.joystick.get_axis(0) < -0.10:
                    self.x = 1
                else:
                    self.x = 0

                if self.joystick.get_axis(1) > 0.10:
                    self.y = 1
                elif self.joystick.get_axis(1) < -0.10:
                    self.y = -1
                else:
                    self.y = 0

            if event.type == pygame.JOYBUTTONDOWN:
                pass
                # print("Joystick Button pressed")
        return self.x, self.y


# Simple example of usage
if __name__ == '__main__':
    joystick = Joystick()

    while True:
        coord = joystick.getEvents()
        print(coord)
