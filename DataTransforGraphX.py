#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/3/19 20:40
#!@Author : zyy
#!@File   : DataTransforGraphX.py

print("hello,world")


#filename='D:\Datasets\\test.txt'
#fileNew = 'D:\Datasets\\testGraphX.txt'

filename='D:\Datasets\com-friendster.ungraph\com-friendster.ungraph.txt'
fileNew = 'D:\Datasets\\friGraphX.txt'
fobj = open(fileNew, 'wb+')
with open(filename,'r') as f:
    next(f)
    next(f)
    next(f)
    next(f)
    #skip first four lines
    for line in f:
        line = line.replace('\n', '')  # 去掉换行符，需要注意
        print(line)
        res = line.split()
        srcid = res[0]
        dstid = res[1]
        input = srcid+' '+dstid+'\n'
        input1 = bytes(input,encoding="utf8")
        fobj.write(input1)




f.close()
fobj.close()
