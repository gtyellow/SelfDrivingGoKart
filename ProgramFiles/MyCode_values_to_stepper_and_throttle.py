#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import dependencies


# In[2]:


#load model


# In[ ]:


#load arduino
#you also need to flash firmata express to arduino

port='COM4'
arduinoUno = pymata4.Pymata4()

#connect to autonomous vehicle
connectionResult = connect(port)

while connectionResult != "success":
    print("arduino failed to connect but trying again...")
    connectionResult = connect(port)

print("arduino connected!")

time.sleep(3)


# In[ ]:


#setup and test connections to stepper, steeering sensor and throttle.  


# In[3]:


#get min, max of steering sensor and throttle
steerSensorPin = 1
throttleSensorPin = 2



minSteerSensorValue = 10000
maxSteerSensorValue = -10000

minThrottleSensorValue = 10000
maxThrottleSensorValue = -10000

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

time.sleep(1)

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


# In[ ]:


#calibrate stepper to 0% steering angle


# In[ ]:


#handles all writing to disk
import os
import cv2
import datetime
import json
import math
import pandas as pd

dataName = None 
inImageWriter = None 
outImageWriter = None 
debugFile = None
data_dir = None

def setupWriter(debug):
    global dataName, inImageWriter, outImageWriter, debugFile, data_dir

    dataName = input("please type name of this run. This will be the name of the Data folder> ")

    current_directory = os.getcwd()
    data_dir = os.path.join(current_directory, dataName)
    try:
        os.mkdir(data_dir)
        print("Directory " , data_dir ,  " Created ") 
    except FileExistsError:
        print("Directory " , data_dir ,  " already exists")

    if debug:
        debug_dir = os.path.join(current_directory, "DEBUG_" + dataName)
        try:
            os.mkdir(debug_dir)
            print("Directory " , debug_dir ,  " Created ") 
        except FileExistsError:
            print("Directory " , debug_dir ,  " already exists")
        
        inImagePath = os.path.join(debug_dir, "InImage.avi")
        inImageWriter = cv2.VideoWriter(inImagePath,cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,(512,256))
        outImagePath = os.path.join(debug_dir, "OutImage.avi")
        outImageWriter = cv2.VideoWriter(outImagePath,cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,(512,256))

        debugFilePath = os.path.join(debug_dir, "DebugMessage.txt")
        debugFile = open(debugFilePath, "w")

#Train data 
def writeVerifyData(actual_angle, throttle, predicted_angle, image, framecount):
    global record_df, record_list

    camName = str(framecount) + '_cam_image_array.jpg'
    camPath = os.path.join(data_dir, camName)
    cv2.imwrite(camPath, image) 
    
    #record_row={'image_num': camName, 'angle': angle, 'throttle%': throttle}
    record_row=[camName, actual_angle, predicted_angle, throttle]

    record_list.append(record_row)
    return record_list


# In[ ]:


#For saving the verification data
setupWriter(False)


# In[ ]:


#test camera to see if its working
#this code checks to see if camera is working and also saves data
#it also captures current steering sensor data

cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened()== False): 
    print("Error opening video stream or file")

count=0
record_list = []
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        #since we preprocessed in training, we need to preprocess during prdiction
        img=np.asarray(frame)
        img=preProcessing(img)
        img=np.array(img)

        desired_steering, desired_throttle = float(model.predict(img))

        print("Desired steering -> "+ desired_steering, " Desired throttle ->"+ desired_throttle)
        
        ###!!! Need to covnert desired steering to number of steps and then feed desired steps to arduino
        
        
        # Display the resulting frame
        cv2.imshow('Frame',frame)
        
        
        
        currentSteeringReading, time_stamp = arduinoUno.analog_read(steerSensorPin)
        currentThrottleReading, time_stamp=desired_throttle
        
        
        #writes verifcation data
        writeVerifyData(SteerSensorValueToAngle(currentSteeringReading), ThrottleSensorValuetoPercentage(currentThrottleReading), predicted_angle, frame, count)
        count+=1

 
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
 
        # Break the loop
    else: 
        break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
record_df = pd.DataFrame(record_list)
record_path=os.path.join(data_dir, 'results.csv')
record_df.to_csv(record_path, index=False, header=False)


# In[ ]:


#find out how many steps per steering degree


# In[ ]:


#load frame data into predition
#output should be desired steering angle and desired throttle

#feed desired throttle to throttle pin

#Desired steering angle minus current steering angle
#convert to steps
#feed number of steps to stepper

# probably need some sort fo check that steps are workings

