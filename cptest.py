import os
import random
import shutil
from shutil import copyfile

ftest = open('data/test.txt')
lines = ftest.readlines()
i = 0
for path in lines:
    path = path.replace('\n',"").replace('\r','')
    savepath = "data/samples/"
    savename = savepath + "test" + str(i) +'.jpg'
    i += 1
    print(savename)
    copyfile(path,savename)
