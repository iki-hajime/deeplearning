'''
Created on 2016/09/08

@author: baba1
'''

# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import cPickle

import numpy as np
import six
import cv2
import os
import datetime
import six.moves.cPickle as pickle

import chainer
from chainer import computational_graph as c
from chainer import cuda
import chainer.functions as F
from chainer import optimizers

def detect(image, cascade_file = "./haarcascade_frontalface_default.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)

    faces = cascade.detectMultiScale(image,
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))

    return faces
img = cv2.imread("angry4.png")
#img = cv2.imread(sys.argv[1])

faces = detect(img)

today  =    datetime.date.today()
todaydetail  =    datetime.datetime.today()


if os.path.exists(str(today)):
    pass
else:
    os.mkdir(str(today))

faceframenum = 0

for (x, y, w, h) in faces:
    dst = img[y:y+h, x:x+w]
    dst = cv2.resize(dst, (100, 100))
    cv2.imwrite("./" + str(today) + "/"  + str(todaydetail.hour).zfill(2) +
            str(todaydetail.minute).zfill(2) + str(todaydetail.second).zfill(2) +
            str(todaydetail.microsecond).zfill(6)  + str(faceframenum) + ".jpg", dst)
    faceframenum += 1
