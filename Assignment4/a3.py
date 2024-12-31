# import cv2 as cv
# import numpy as np

# img = cv.imread('a.png',cv.IMREAD_COLOR) # reading the colour image 
# if img is None:
#     print("Error: Unable to read the image")
# else:
#     filter_matrix = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]) #creating the Filter matrix
#     filtered_image = cv.filter2D(img, -1, filter_matrix) #applying the filter
#     cv.imshow('Filtered Image', filtered_image) #image after applying Filter
#     cv.waitKey(0)

import cv2
import numpy as np

img = cv2.imread('a.png',cv2.IMREAD_COLOR) #reading the colour image
if img is None:
    print("Error: Unable to read the image")
else:
    P = np.array(img)
    X = np.mean(P,axis=2).astype(np.uint8) #converting into gray scale
    _,Z50 = cv2.threshold(X,50,255,cv2.THRESH_BINARY) #Binarized image with threshold 50
    cv2.imshow("Binarized image (Threshold 50)",Z50) #Showing binarized image with threshold 50
    _,Z70 = cv2.threshold(X,70,255,cv2.THRESH_BINARY) #Binarized image with threshold 70
    cv2.imshow("Binarized image (Threshold 70)",Z70) #Showing binarized image with threshold 70
    _,Z100 = cv2.threshold(X,100,255,cv2.THRESH_BINARY) #Binarized image with threshold 100
    cv2.imshow("Binarized image (Threshold 100)",Z100) #Showing binarized image with threshold 100
    _,Z150 = cv2.threshold(X,150,255,cv2.THRESH_BINARY) #Binarized image with threshold 150
    cv2.imshow("Binarized image (Threshold 150)",Z150) #Showing binarized image with threshold 150
    cv2.waitKey(0)
