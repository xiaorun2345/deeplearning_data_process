import os
import shutil
data_file="/home/lenovo/Desktop/final-data"
Annotations="/home/lenovo/Desktop/final-data/Annotations"
JPEGImages="/home/lenovo/Desktop/final-data/JPEGImages/"
classes=['3.0','3.5','3.75','4.0','4.5']
xml_img=os.listdir(data_file)
for classfile in classes:
    absolute_path=os.path.join(data_file,classfile)
    print (absolute_path)
    for xml_and_jpg in os.listdir(absolute_path):
        jpgfile=xml_and_jpg.split('.')[-1]
        print(jpgfile)
        allpath =absolute_path+'/'+xml_and_jpg
        print(allpath)
        if jpgfile=="jpg":
            old_path=absolute_path+"/"+xml_and_jpg
            print(old_path)
            ImagePath=JPEGImages+xml_and_jpg
            shutil.copyfile(old_path, ImagePath)
        if jpgfile=='xml':

            old_annotions=absolute_path+"/"+xml_and_jpg
            Annotations_path=Annotations+'/'+xml_and_jpg
            shutil.copyfile(old_annotions,Annotations_path)