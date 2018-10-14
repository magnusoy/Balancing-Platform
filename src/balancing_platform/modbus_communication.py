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
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient


class ModbusClient(object):
    """docstring"""
    def __init__(self, ip='192.168.2.17'):
        self.ip = ip
        self.client = ModbusTcpClient(self.ip)
        self.connection = self.client.connect()

    def isConnected(self):
        """docstring"""
        return self.connection

    def send(self, value, address):
        """docstring"""
        builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        builder.add_32bit_int(value)
        payload = builder.build()
        result = self.client.write_registers(address, payload, skip_encode=True, unit=1)
        return result

    def read(self, address):
        """docstring"""
        result = self.client.read_holding_registers(address, 2, unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
        return str(decoder.decode_32bit_float())

    def close(self):
        """docstring"""
        self.client.close()
        return True


if __name__ == '__main__':
    client = ModbusClient()
    while client.isConnected():
        client.read(address=12288)
