import cv2
import numpy as np 

im = cv2.imread('test/some_16.jpg')

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
for a in range(1,2000):
	img = cv2.drawContours (im, contours, a, (0, 0, 255), 3)

resized_image = cv2.resize(im, (600, 600)) 

cv2.imshow("img", resized_image)

cv2.waitKey(0)
