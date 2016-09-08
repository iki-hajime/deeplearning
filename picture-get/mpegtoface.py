import sys
import numpy as np
import cv2
import datetime
import os
import shutil


cascade_path = "./haarcascade_frontalface_default.xml"
#cascade_path = "./haarcascade_frontalface_alt_tree.xml"
#cascade_path = "./haarcascade_frontalface_alt.xml"
#cascade_path = "/Path/To/.pyenv/versions/anaconda-2.1.0/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

def detectFace(image):
    cascade = cv2.CascadeClassifier(cascade_path)
    image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
    image_gray = cv2.equalizeHist(image_gray)
    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(50, 50))
    print "finding......"
    print facerect
    return facerect

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('bbb.mp4')
today  =    datetime.date.today()
todaydetail  =    datetime.datetime.today()


if os.path.exists(str(today)):
    pass	
else:
    os.mkdir(str(today))

#    shutil.rmtree(str(today))

framenum = 0
faceframenum = 0

while(1):
    framenum += 1
    ret, image = cap.read()
    if not ret:
        break
    if framenum%17==0:
        facerect = detectFace(image)
        if len(facerect) == 0: continue

        for rect in facerect:
            todaydetail  =    datetime.datetime.today()
            croped = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
            croped1 = cv2.resize(croped,(100,100))
            cv2.imwrite("./" + str(today) + "/"  + str(todaydetail.hour).zfill(2) + 
                        str(todaydetail.minute).zfill(2) + str(todaydetail.second).zfill(2) + 
                        str(todaydetail.microsecond).zfill(6)  + str(faceframenum) + ".jpg", croped1)
            print "I found the human!"
            faceframenum += 1

cap.release()