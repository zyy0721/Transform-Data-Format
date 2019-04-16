#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/4/15 15:21
#!@Author : zyy
#!@File   : DataTransforSouffle.py

#filename='D:\Datasets\\test.txt'
#fileNew = 'D:\Datasets\\edge.facts'

filename='D:\Datasets\com-friendster.ungraph\com-friendster.ungraph.txt'
fileNew = 'D:\Datasets\Souffle\\friedge.facts'
fobj = open(fileNew, 'wb+')
with open(filename,'r') as f:
    next(f)
    next(f)
    next(f)
    next(f)
    #skip first four lines
    for line in f:
        print(line)
        input12 = bytes(line,encoding="utf8")
        fobj.write(input12)




f.close()
fobj.close()
print("Finished!")