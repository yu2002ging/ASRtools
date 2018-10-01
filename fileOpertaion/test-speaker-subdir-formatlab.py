# -*- coding: utf-8 -*-

import os
import shutil

pathway = u'C:/Users/xiawuyang/Desktop/多媒体语音数据集/dataset/'  # u  because it has chinese words
targetway = 'C:/Users/xiawuyang/Desktop/test/'
for file1 in os.listdir(pathway):
    if file1[:2].isdigit():
        p1 = os.path.join(pathway, file1)
        gate = 0
        for file2 in os.listdir(p1):
            if file2.endswith('wav'):
                dirname = file1         # eg: 00liu
                filename = file2[:4]    # eg: 0910
                target = os.path.join(targetway, dirname)
                if gate == 0:
                    os.mkdir(target)
                targetd = os.path.join(target, filename)  #eg: C:\Users\xiawuyang\Desktop\test\00liu\0910\
                srcf = os.path.join(p1, file2)
                targetf = os.path.join(targetd, file2)
                os.mkdir(targetd)
                print(srcf)
                shutil.copy(srcf, targetf)
                gate += 1
