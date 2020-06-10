# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:39:56 2020

@author: siddh
"""

import cv2
import argparse
import sys
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

if len(sys.argv)==2:
    img = cv2.imread(sys.argv[1])
    cv2.imshow('cropped',img)
    print(pytesseract.image_to_string(img))

elif len(sys.argv)<2:
	print("Enter second argument as image")

else:
	print("Too many arguments")
	print("Filename and path to image")