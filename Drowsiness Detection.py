#!/usr/bin/env python
# coding: utf-8

# In[14]:


import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
import time


# In[15]:


mixer.init()
sound = mixer.Sound(r'C:\Users\houce\Downloads\Driver-Drowsiness-Detection-using-Deep-Learning-main\Driver-Drowsiness-Detection-using-Deep-Learning-main\alarm.wav')

face_cascade = cv2.CascadeClassifier(r'C:\Users\houce\Downloads\Driver-Drowsiness-Detection-using-Deep-Learning-main\Driver-Drowsiness-Detection-using-Deep-Learning-main\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\houce\Downloads\Driver-Drowsiness-Detection-using-Deep-Learning-main\Driver-Drowsiness-Detection-using-Deep-Learning-main\haarcascade_eye.xml')
model = load_model(os.path.join(r'C:\Users\houce\Downloads\Driver-Drowsiness-Detection-using-Deep-Learning-main\Driver-Drowsiness-Detection-using-Deep-Learning-main\models'))






# In[ ]:





# In[17]:


path = os.getcwd()
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
score = 0

while(True):
    ret, frame = cap.read()
    height,width = frame.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,minNeighbors = 3,scaleFactor = 1.1,minSize=(25,25))
    eyes = eye_cascade.detectMultiScale(gray,minNeighbors = 1,scaleFactor = 1.1)

    cv2.rectangle(frame, (0,height-50) , (200,height) , (0,0,0) , thickness=cv2.FILLED )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y) , (x+w,y+h) , (255,0,0) , 3 )

    for (x,y,w,h) in eyes:

        eye = frame[y:y+h,x:x+w]
        #eye = cv2.cvtColor(eye,cv2.COLOR_BGR2GRAY)
        eye = cv2.resize(eye,(80,80))
        eye = eye/255
        eye = eye.reshape(80,80,3)
        eye = np.expand_dims(eye,axis=0)
        prediction = model.predict(eye)
        print(prediction)
       #Condition for Close
        if prediction[0][0]>0.30:
            cv2.putText(frame,"Closed",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'Score:'+str(score),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            score=score+1
           
            if(score > 2):
                try:
                    sound.play()
                except:  
                    pass

        #Condition for Open
        elif prediction[0][1] > 0.70:
            score = score - 1
            if (score < 0):
                score = 0
            cv2.putText(frame,"Open",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            
            cv2.putText(frame,'Score:'+str(score),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()






