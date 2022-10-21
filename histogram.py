import matplotlib.pyplot as plt
import os
import numpy as np
import glob
import pandas as pd
import csv
import cv2
import imutils
from os import listdir

#wayofpython
inputPath = input('Path: ')  
outputpath =inputPath + 'histogram/'
folder_dir=inputPath
for images in os.listdir(folder_dir):
    if(images.endswith(".png")) :
        filepath=inputPath+images #get duong dan file
        filename = images  #get file name
        outputfilepath = outputpath+images
        #print(filename)

sizeImage = 250
I = cv2.imread(filepath)
plt.imshow(I)
#cv2.imshow('Displaying Images',I)
I=cv2.resize(I,[sizeImage,sizeImage])
I=cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
plt.imshow(I)
angle = 180
arrAA=[]
n=0
I = imutils.rotate(I,angle)
plt.imshow(I)
#cv2.imshow("Rotated",I)
mFileName = {filename}
arrhistvalue=[]
arrfilename=[]
arrFileName = [arrfilename,mFileName]

#### Histogram ####
