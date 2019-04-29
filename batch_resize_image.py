import cv2
import numpy as np
import os

Pathname="/home/lenovo/Downloads/neg/neg"
SavePath="/home/lenovo/Downloads/New/Neg"
i=1
imgList=os.listdir(Pathname)
for img in imgList:
    absolutePath=os.path.join(Pathname,img)
    #print absolutePath
    img_Name=cv2.imread(absolutePath)
    resize_img=cv2.resize(img_Name,(64,128))
    New_Path=SavePath+'/'+str(i)+".jpg"
    print New_Path
    cv2.imwrite(New_Path,resize_img)
    i=i+1