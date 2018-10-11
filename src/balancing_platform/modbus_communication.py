#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Communicate with PLC though
Modbus-communication. Sending and
receiving data.

Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/
"""

# Importing packages
from pymodbus.client.sync import ModbusTcpClient


class Communication(object):

    def __init__(self, ip='127.0.0.1'):
        self.ip = ip
        self.client = ModbusTcpClient(self.ip)

    def send(self):
        self.client.write_coil(1, True)

    def receive(self):
        result = self.client.read_coils()
        return result.bits[0]

    def close(self):
        self.client.close()
        return True


if __name__ == '__main__':
    comm = Communication()
