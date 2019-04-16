#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/4/16 15:26
#!@Author : zyy
#!@File   : DataTransforcsvtofacts.py

#filename='D:\Datasets\\testcircle.csv'
#fileNew = 'D:\Datasets\\testcircle.facts'

filename='D:\Datasets\\tree11.csv'
fileNew = 'D:\Datasets\\tree11.facts'
fobj = open(fileNew, 'wb+')
with open(filename,'r') as f:
    for line in f:
        line = line.replace('\n', '')  # 去掉换行符，需要注意
        print(line)
        res = line.split(',')
        srcid = res[0]
        dstid = res[1]
        input = srcid + '\t' + dstid + '\n'
        input1 = bytes(input, encoding="utf8")
        fobj.write(input1)





f.close()
fobj.close()
print("Finished!")