import os
import random
import shutil
 
trainval_percent = 0.9
train_percent = 0.9
filepath = '../Webcam'
txtsavepath = 'data/imgset'
labelsavepath = 'data/labels'
imgspath = 'data/imgs'
total_xml = os.listdir(filepath)
total_img = [d for d in total_xml if d[-3:]=='jpg']
total_label = [d for d in total_xml if d[-3:] == 'txt']

"""
for label_name in total_img:
    oldpath = os.path.join(filepath, label_name)
    newpath = os.path.join(imgspath, label_name)
    shutil.copyfile(oldpath,newpath)

"""

num = len(total_img)
l = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(l, tv)
train = random.sample(trainval, tr)
 
ftrainval = open('data/trainval.txt', 'w')
ftest = open('data/test.txt', 'w')
ftrain = open('data/train.txt', 'w')
fval = open('data/val.txt', 'w')
 
for i in l:
    name = 'data/images/' + total_img[i] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
 
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
