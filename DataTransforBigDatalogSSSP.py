#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/3/21 16:27
#!@Author : zyy
#!@File   : DataTransforBigDatalogSSSP.py

#filename='D:\Datasets\\test.txt'
#fileNew = 'D:\Datasets\\testBDLsssp.csv'

filename='D:\Datasets\web-Google\web-Google.txt'
fileNew = 'D:\Datasets\web-GoogleBDLsp.csv'
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
        input = srcid+','+dstid+','+'1'+'\n'
        input1 = bytes(input,encoding="utf8")
        fobj.write(input1)




f.close()
fobj.close()