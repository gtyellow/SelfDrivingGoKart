#!/usr/bin/env python
# coding: utf-8

# In[1]:



import sys
from pymata4 import pymata4
#from pyfirmata import Arduino, util
from pyfirmata import util
import time


# In[2]:


# Change this port to your arduino.  Possibly can find on the bottom righthand corner of your Arduino sketch after connecting
port='COM4'

arduinoUno = pymata4.Pymata4(port)


# In[3]:


it = util.Iterator(arduinoUno)
it.start()


# In[5]:


steerSensorPin = 1
throttleSensorPin = 2

#currentSteeringAngle=arduinoUno.set_pin_mode_analog_input(steerSensorPin)
#currentThrottleReading=arduinoUno.set_pin_mode_analog_input(throttleSensorPin)


#from vehicleSerial import *
#from Sensor_Value_Capture(VehicleSerial.py) import *



minSteerSensorValue = 1000
maxSteerSensorValue = 0

minThrottleSensorValue = 1000
maxThrottleSensorValue = 0

"""
#connect to autonomous vehicle
connectionResult = connect(port)

while connectionResult != "success":
    print("arduino failed to connect but trying again...")
    connectionResult = connect(port)

print("arduino connected!")

time.sleep(3)
"""
print("please turn the steering wheel and throttle multiple times from minimum to maximum states. Then close this program")

time.sleep(4)

while True:
    arduinoUno.set_pin_mode_analog_input(steerSensorPin)
    arduinoUno.set_pin_mode_analog_input(throttleSensorPin)
    currentSteeringReading, time_stamp = arduinoUno.analog_read(steerSensorPin)
    currentThrottleReading, time_stamp=arduinoUno.analog_read(throttleSensorPin)
    


    if currentSteeringReading != None or currentThrottleReading != None:

        if currentSteeringReading < minSteerSensorValue:
            minSteerSensorValue = currentSteeringReading
        elif currentSteeringReading > maxSteerSensorValue:
            maxSteerSensorValue = currentSteeringReading
        
        if currentThrottleReading < minThrottleSensorValue:
            minThrottleSensorValue = currentThrottleReading
        elif currentThrottleReading > maxThrottleSensorValue:
            maxThrottleSensorValue = currentThrottleReading

        print("minSteerSensorValue > " + str(minSteerSensorValue) + " maxSteerSensorValue > " + str(maxSteerSensorValue) + " minThrottleSensorValue > " + str(minThrottleSensorValue) + " maxThrottleSensorValue > " + str(maxThrottleSensorValue))

    else:
        
        if currentSteeringReading == None and currentThrottleReading == None:
            print("Steering and throttle sensors not recording. Check connections")
        elif currentSteeringReading == None:
            print("Steering sensor not recording.  Check connections")
        else:
            print("Throttle sensor not recording.  Check connections")
    
    time.sleep(0.1) 


# In[65]:


# Convert steering sensor to angle.  
# Based on some measurements, I believe the wheels traverse about 56 degrees

minSteerAngle=-23
maxSteerAngle=23

def SteerSensorValueToAngle(currentSteeringReading):
    minSteerAngle=-23
    maxSteerAngle=23
    currentSteerAngle=(currentSteeringReading-minSteerSensorValue)/(maxSteerSensorValue-minSteerSensorValue)*(maxSteerAngle-minSteerAngle)+minSteerAngle
    return currentSteerAngle


def ThrottleSensorValuetoPercentage(currentThrottleReading):
    currentThrottlePercentage=round((currentThrottleReading-minThrottleSensorValue)/(maxThrottleSensorValue-minThrottleSensorValue)*100,1)
    return currentThrottlePercentage


# In[66]:


print(str(SteerSensorValueToAngle(465))+" degrees")
print(str(ThrottleSensorValuetoPercentage(511))+"%")


# In[ ]:


SelfDrivingGoKartFromATVToy\pleasework

