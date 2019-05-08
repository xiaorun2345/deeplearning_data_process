import os
import shutil
imgfiles="/home/lenovo/darknet/scripts/VOCdevkit/VOC2007/JPEGImages"
infile=open("/home/lenovo/darknet/scripts/VOCdevkit/VOC2007/ImageSets/Main/test.txt").read().splitlines()
testdata="/home/lenovo/darknet/scripts/testdata/"
#print(infile)

for imgfile in infile:
    #print(infile)
    image=imgfile+'.jpg'
    absoluteFile=os.path.join(imgfiles,image)
    print(absoluteFile)
    newPath=testdata+image
    shutil.copyfile(absoluteFile,newPath)