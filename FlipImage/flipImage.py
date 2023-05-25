from PIL import Image
 
original_img = Image.open("E:\\Digital_Image_Processing\\image-processing-workshop-master\\FlipImage\\wallpaper.jpg")
 
vertical_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save("E:\Digital_Image_Processing\image-processing-workshop-master\FlipImage\\vertical.jpg")

original_img.close()
vertical_img.close()