import cv2
import sys
import glob 
import os
from shutil import copyfile
from darknet import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as gImage

def draw_bounding_box(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = class_id
    color = COLORS[0]
    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


training_set = []
training_target = []
for k in range(870,879):
    COLORS = np.random.uniform(0, 255, size=(200, 3))

    net = load_net("cfg/yolov3.cfg", "yolov3.weights", 0)
    meta = load_meta("cfg/coco.data")
    img = gImage.imread('data/'+str(k)+'.jpg')
    r = detect(net, meta, 'data/'+str(k)+'.jpg')

    print('number of boxes', len(r))
    box_list = []
    for i in range(len(r)):
        box_list.append([r[i][0], r[i][1], r[i][2][0], r[i][2][1], r[i][2][2], r[i][2][3]])
    print('image', k)
    for i in range(len(box_list)):
        print('box', i, box_list[i])
        x_1 = int(box_list[i][2]-box_list[i][4]/2)
        y_1 = int(box_list[i][3]-box_list[i][5]/2)
        x_2 = int(box_list[i][2]+box_list[i][4]/2)
        y_2 = int(box_list[i][3]+box_list[i][5]/2)
        box_list[i][2] = x_1
        box_list[i][3] = y_1
        box_list[i][4] = x_2
        box_list[i][5] = y_2
        draw_bounding_box(img, str(i), box_list[i][1], box_list[i][2], box_list[i][3], box_list[i][4], box_list[i][5])
        training_set.append([r[i][2][0], r[i][2][1], r[i][2][2], r[i][2][3]])
    plt.imshow(img)
    plt.show()
    for i in range(len(box_list)):
        temp = input('is box '+str(i)+' safe')
        training_target.append(temp)
    print('training_set length', np.array(training_set).shape)
    print('training_target length', np.array(training_target).shape)
    
#np.save('training_set.npy', training_set)
#np.save('training_target.npy',training_target)

np.savetxt('x.csv', training_set, delimiter = ',')
np.savetxt('y.csv', training_target, delimiter = ',')
