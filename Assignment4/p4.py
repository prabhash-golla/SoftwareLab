import cv2 as cv
import numpy as np

#blank
# blank = np.zeros((img.shape[0],img.shape[1],3),dtype='uint8')
# cv.imshow("blank",blank)

#rectangle
# rect = cv.rectangle(blank,(0,0),(250,250),(255,255,255),thickness=5)
# cv.imshow("rect",rect)

#circle 
# cir = cv.circle(blank,(250,250),10,(0,55,0),thickness=-1)
# cir = cv.circle(blank,(220,250),10,(0,255,0),thickness=-1)
# cv.imshow("cir",cir)

#line
# line = cv.line(blank,(250,250),(340,340),(122,0,0),thickness=1)
# cv.imshow("line",line)

img = cv.imread('a.png',cv.IMREAD_COLOR)
cv.imshow('Image',img)

#grey sacle 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur
blur = cv.blur(img,(7,7))
cv.imshow('Blur',blur)

#edges
cannny = cv.Canny(blur,100,10)
cv.imshow('canny',cannny)

cv.waitKey(0)
cv.destroyAllWindows()