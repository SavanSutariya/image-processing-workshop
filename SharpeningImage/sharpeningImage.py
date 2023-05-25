import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("E:\\Digital_Image_Processing\\image-processing-workshop-master\\SharpeningImage\\wallpaper.jpg", 0)

# try 2nd Matrix with 4 to 5 and then run - it will better sharp at border 
k2 = np.array(([[0, -1, 0],
                   [-1, 4,-1],
                   [0, -1, 0]]), np.float32)

print(k2)
output = cv2.filter2D(img, -1, k2)
plt.subplot(1,2,1)
plt.imshow(img, 'gray')
plt.title('Original Image')
plt.subplot(1,2,2)
plt.imshow(output, 'gray')
plt.title('Filterd Image')
plt.show()