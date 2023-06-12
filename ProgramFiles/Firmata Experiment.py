#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install pyfirmata')


# In[20]:


get_ipython().system('pip3 install pymata')


# In[17]:


import pandas as pd


# In[22]:


from pymata4 import pymata4


# In[2]:


from pyfirmata import Arduino
import time
from time import sleep


# In[3]:


import pyfirmata


# In[4]:


if __name__ == '__main__':
    board = Arduino('COM4')
    print("Communication Successfully started")


# In[5]:


# pin for sensor
pin = board.get_pin('a:1:i') #analog pin A# . the # is the pin number in the middle of the colons


# In[6]:


#this is all for the potentiometer
it = pyfirmata.util.Iterator(board)
it.start()

while True:
    analog_value= pin.read()
    print(analog_value)
    time.sleep(0.1)


# In[26]:


if __name__ == '__main__':
    board = pymata4.Pymata4()
    print("Communication Successfully started")


# In[8]:


#control stepper motor

num_steps =5  # number of steps
pins = [8,9,10,11] #pin numbers


# In[27]:


# set pins for stepper motor

board.set_pin_mode_stepper(num_steps, pins)


# In[30]:


while True:
    board.stepper_write(21, num_steps)
    time.sleep(1)
    board.stepper_write(21, -5)
    time.sleep(.5)


# In[ ]:


LEDs =[LED1,LED2,LED3]
LED_index=0
previous_button_state=0


# In[ ]:


# Start iterator to receive input data
it = pyfirmata.util.Iterator(board)
it.start()


# In[ ]:


button.mode=pyfirmata.INPUT


# In[ ]:


for LED in LEDs:
    LED.write(0)


# In[ ]:


# the "void loop()"
while True:
    #we run the loop at 100Hz
    time.sleep(0.01)
    
    #Get button current state
    button_state = button.read()
    
    #check if button has been released
    if button_state != previous_button_state:
        if button_state ==0:
            print ("Button Released")
            
            #power off current LED
            # and power on next LED
            
            LEDs[LED_index].write(0)
            print("I sent a signal")
            LED_index +=1
            if LED_index >= len (LEDs):
                LED_index=0
            LEDs[LED_index].write(1)
                 
    #save current buttone state as previous
    #for the next loop iteration
    previous_button_state=button_state
                 


# In[ ]:





# In[ ]:




