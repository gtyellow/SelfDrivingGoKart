#!/usr/bin/env python
# coding: utf-8

# In[1]:


#first upload firmata express to arduino


# In[2]:


import time
from pymata4 import pymata4


# In[8]:


num_steps = 200
rev_num_steps = 200
pins = [8,9] #can use 2 or 4 pins depending on stepper
board=pymata4.Pymata4()

board.set_pin_mode_stepper(num_steps, pins)

steerSensorPin = 1
throttleSensorPin = 2

board.set_pin_mode_analog_input(steerSensorPin)
board.set_pin_mode_analog_input(throttleSensorPin)


# In[9]:





while True:
    
    
    steerSensorValue, time_stamp = board.analog_read(steerSensorPin)
    print("Steer Sensor value ->" + str(steerSensorValue))
    throttleSensorValue, time_stamp=board.analog_read(throttleSensorPin)
    print("Throttle Sensor Value" + str(throttleSensorValue))
    
    
    board.stepper_write(300, num_steps)
    time.sleep(1)
    board.stepper_write(300, rev_num_steps)
    time.sleep(.5)
    

    


# In[6]:


board.stepper_read


# In[ ]:





# In[ ]:




