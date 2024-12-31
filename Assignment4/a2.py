import cv2
import numpy as np
import time
img = cv2.imread('a.png',cv2.IMREAD_COLOR)
if img is None:
    print("Error: Unable to read the image")
else:
    cv2.imshow('Given Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    X = np.array(grayscale_img)
    Y=X.copy()
    Z=np.multiply(X,Y)
    
    starttime = time.time()
    Z=X*Y
    endtime = time.time()
    print("Time for numpy multiplication : ",endtime-starttime,"seconds")
    print(Z[0])
    print(Z.size)

    height, width = len(X), len(X[0])
    starttime = time.time()
    for i in range(height):
        for j in range(width):
            Y[i][j] = X[i][j]
    Z1 = [[0] * X.shape[1] for _ in range(X.shape[0])]
    for i in range(height):
        for j in range(width):
            Z1[i][j] = X[i][j]*Y[i][j]
    # Z1=[[int(X[i][j]) * int(Y[i][j]) for j in range(width)] for i in range(height)]
    endtime = time.time()
    print("Time for normal multiplication : ",endtime-starttime,"seconds")

    if(np.array_equal(Z,Z1)):
        print("YES YES")
    else:
        print("NOOO")
