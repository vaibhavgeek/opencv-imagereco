import cv2
import numpy as np

#######   training part    ############### 
samples = np.loadtxt('generalsamples.data',np.float32)
responses = np.loadtxt('generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.KNearest()
model.train(samples,responses)

############################# testing part  #########################

image_max = cv2.imread('test/some_8.jpg')
print image_max.shape
im = image_max[100:3204, 200:300] # Crop from x, y, w, h -> 100, 200, 300, 400

out = np.zeros(im.shape,np.uint8)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if  h>28:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.find_nearest(roismall, k = 1)
            string = str(int((results[0][0])))  
            cv2.putText(out,string,(x,y+h),0,1,(0,255,0))

#cv2.imshow('im',im)
resized_im = cv2.resize(im, (500, 500)) 
cv2.imshow("img", im)

resized_out = cv2.resize(out, (500,500))
cv2.imshow("out",out)
cv2.imwrite('test/output.png', out)

cv2.waitKey(0)