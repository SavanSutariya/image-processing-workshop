import cv2
from matplotlib import pyplot as plt

img = cv2.imread("E:\\Digital_Image_Processing\\image-processing-workshop-master\\ImageHistogram\\wallpaper.jpg", 0)


hist1 = cv2.calcHist([img], [0], None, [256], [0,256])
img2 = cv2.equalizeHist(img)
hist2 = cv2.calcHist([img2], [0], None, [256], [0,256])
plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR));
plt.subplot(222), plt.plot(hist1);
plt.subplot(223), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BAYER_BG2BGR));
plt.subplot(224), plt.plot(hist1);

plt.plot(hist1)
plt.plot(hist2)
plt.show()