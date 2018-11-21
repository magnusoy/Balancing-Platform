#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modbus TCP Client Test

Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing package
from src.balancing_platform.modbus_communication import ModbusClient

# Run test
if __name__ == '__main__':
    client = ModbusClient(ip='192.168.2.17')

    while client.isConnected():
        response = client.readInt(address=12288, size=20)
        print(response)
