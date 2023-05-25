import cv2
import numpy as np

img = cv2.imread("E:\\Digital_Image_Processing\\image-processing-workshop-master\\GeomatricTransform\\wallpaper.jpg", 1)
rows, cols, ch = img.shape

matrix_trans = np.float32([[1,0, 100], [0, 1, 30]])
traslated_img = cv2.warpAffine(img, matrix_trans, (cols, rows))

cv2.imshow("Translate Image", traslated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
