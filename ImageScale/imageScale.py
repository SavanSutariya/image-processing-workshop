import cv2
import numpy as np

img = cv2.imread("E:\\Digital_Image_Processing\\image-processing-workshop-master\\GeomatricTransform\\wallpaper.jpg", 1)
sacle_img = cv2.resize(img, None, fx=2, fy=2)

cv2.imshow("Scale Image", sacle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
