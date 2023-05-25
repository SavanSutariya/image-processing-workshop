import cv2

imgPath = "E:\Digital_Image_Processing\DisplayImageProperties\wallpaper.jpg"

img1 = cv2.imread(imgPath, 1)
print(type(img1))

print('Image Data Type:', img1.dtype)
print('Row Column:', img1.shape)
print('Dimention:', img1.ndim)
print('Image Size:', img1.size)

(nr,nc,ch)=img1.shape

print('No. of Rows:', nr)
print('No. of Column:', nc)
print('No. of Channels:', ch)

cv2.imshow('Lena', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()