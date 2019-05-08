import os
import cv2
import numpy as np

path = '/home/lenovo/ssd/caffe/examples/ssd/images'
filelist = os.listdir(path)

fps = 10
size = (1279, 720)
fourcc = cv2.VideoWriter_fourcc(*'mpeg')
video = cv2.VideoWriter("/home/lenovo/ssd/caffe/VideoTest1.mp4", fourcc, fps, size)
print(filelist)
for item in filelist:
    #if item.endswith('.png'):
    image= os.path.join(path,item)
    img = cv2.imread(image)
    img=cv2.resize(img,(1279,720))
    print(img.shape)
    video.write(img)

video.release()
cv2.destroyAllWindows()