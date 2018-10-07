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

# Start a client socket
client = ModbusTcpClient('127.0.0.1')

# Send data
client.write_coil(1, True)

# Read data
result = client.read_coils(1, 1)
print(result.bits[0])

# Closes connection with socket
client.close()
