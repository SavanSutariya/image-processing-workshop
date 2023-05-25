import cv2

img = cv2.imread("E:\Digital Image Processing\ImageGrayScale\wallpaper.jpg", 0)

outpath = "E:\Digital Image Processing\ImageGrayScale\wallpaper1.jpg"

cv2.imshow('Lena', img)
cv2.imwrite(outpath, img)
cv2.waitKey(0)
cv2.destroyAllWindows()