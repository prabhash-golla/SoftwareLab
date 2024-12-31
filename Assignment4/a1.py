# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt

# X = np.ones([200,200,3],dtype=np.uint8)*0
# # K = np.ones([200,200,3],dtype=np.uint8)*0

# arr = cv.imread('a.png')
# arr = cv.cvtColor(arr,cv.COLOR_BGR2RGB)
# Y = cv.circle(X,(100,100),100,(255,255,255),-1)
# # cv.imshow("Circle",Y)
# plt.imshow(arr)
# plt.show()
# # cv.waitKey(0)

# # Z= cv.rectangle(K,(20,20),(180,180),0,-1)
# # cv.imshow("Circle",Z)
# # cv.waitKey(0)

# # A = np.bitwise_xor(Y,Z)
# # cv.imshow("Circle",A)
# # cv.waitKey(0)

import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 10, 10000)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with two subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Plot the first graph on the left subplot
axes[0].plot(x, y1, label='Sin(x)')
axes[0].set_title('Plot 1')
axes[0].legend()

# Plot the second graph on the right subplot
axes[1].plot(x, y2, label='Cos(x)', color='green')
axes[1].set_title('Plot 2')
axes[1].legend()

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()
