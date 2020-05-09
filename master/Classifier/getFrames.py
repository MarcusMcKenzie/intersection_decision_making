import cv2
import sys
import glob 
import os
from shutil import copyfile

directory = '/home/shuo/Downloads/Classifier'
os.chdir(directory)
#f = open("darknet/train.txt", "a")
count = 0
for file in glob.glob('*.MOV'):
	
	name = file[:-4]
          
	vidcap = cv2.VideoCapture(file)
	success,image = vidcap.read()
	print(success)
	
	while success:
	  cv2.imwrite("%d.jpg" % int(count), image)     # save frame as JPEG file    
	  success,image = vidcap.read()
	  count += 1 

