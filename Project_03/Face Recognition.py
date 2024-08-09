#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install opencv-python')


# In[8]:


import cv2


# In[12]:


import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
video_cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_cap.read()
    
    # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Live_Face Detection', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) == ord('a'):
        break

# Release the capture and close all windows
video_cap.release()
cv2.destroyAllWindows()


# In[ ]:




