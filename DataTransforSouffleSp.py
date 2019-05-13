#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/4/17 14:25
#!@Author : zyy
#!@File   : DataTransforSouffleSp.py

import random
#filename='D:\Datasets\\test.txt'
#fileNew = 'D:\Datasets\\edgesp.facts'

filename='D:\Datasets\wiki-Talk\WikiTalk.txt'
fileNew = 'D:\Datasets\Souffle\\wikiedgesp.facts'
fobj = open(fileNew, 'wb+')
with open(filename,'r') as f:
    next(f)
    next(f)
    next(f)
    next(f)
    #skip first four lines
    for line in f:
        line = line.replace('\n', '')  # 去掉换行符，需要注意
        cost = random.randint(1,9)
        linesp = line + '\t' + str(cost) + '\n'
        print(linesp)
        input12 = bytes(linesp,encoding="utf8")
        fobj.write(input12)




f.close()
fobj.close()
print("Finished!")