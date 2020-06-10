# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:30:20 2020

@author: siddh
"""

import cv2
import argparse 
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help = 'path to input image')
ap.add_argument('-c', '--config', required=True,
                help = 'path to yolo config file')
ap.add_argument('-w', '--weights', required=True,
                help = 'path to yolo pre-trained weights')
ap.add_argument('-cl', '--classes', required=True,
                help = 'path to text file containing class names')
args = ap.parse_args()

def get_output(model):
    layer_names = model.getLayerNames()
    output_layers = [layer_names[i[0]-1]for i in model.getUnconnectedOutLayers()]
    return output_layers

def draw_preds(img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    label = str(classes[class_id])

    color = COLORS[class_id]

    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    image=img[y:y_plus_h,x:x_plus_w]
    cv2.imshow('crop',image)
    cv2.imwrite("cropped.jpg",image)

image = cv2.imread(args.image)
Width = image.shape[0]
Height = image.shape[1]
scale_factor = 0.00392
classes = None

with open(args.classes, 'r') as f:
    classes = [line.strip() for line in f.readlines()]


COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

model = cv2.dnn.readNet(args.weights, args.config)

blob = cv2.dnn.blobFromImage(image, scale_factor, (416,416), (0,0,0), True, crop=False)

model.setInput(blob)

outputs = model.forward(get_output(model))

class_ids = []
confidences = []
bounding_boxes = []
conf_threshold = 0.5
nms_threshold = 0.4

for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0]*Width)
            center_y = int(detection[1]*Height)
            w = int(detection[2] * Width)
            h = int(detection[3] * Height)
            x = center_x - w / 2
            y = center_y - h / 2
            class_ids.append(class_id)
            confidences.append(float(confidence))
            bounding_boxes.append([x,y,w,h])
            
indices = cv2.dnn.NMSBoxes(bounding_boxes,confidences,conf_threshold,nms_threshold)

for i in indices:
    i = i[0]
    box = bounding_boxes[i]
    x,y,w,h = box[0],box[1],box[2],box[3]
    draw_preds(image,class_ids[i],confidences[i],round(x),round(y),round(x+w),round(y+h))

cv2.imshow("license plate detection",image)
cv2.waitKey()

cv2.imwrite("plate-detection.jpg",image)
cv2.destroyAllWindows()        