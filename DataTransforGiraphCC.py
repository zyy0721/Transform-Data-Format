#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/3/25 17:21
#!@Author : zyy
#!@File   : DataTransforGiraphCC.py

#filename='D:\Datasets\\test.txt'
#fileNew = 'D:\Datasets\\testforCC.txt'

filename='D:\Datasets\com-friendster.ungraph\com-friendster.ungraph.txt'
fileNew = 'D:\Datasets\\friCC.txt'
fobj = open(fileNew, 'wb+')
allsrcid=set('')
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
        if srcid in allsrcid:
            input = ' '+ dstid
            input1 = bytes(input,encoding="utf8")
            fobj.write(input1)
        else:
            if allsrcid.__len__() != 0:
                inputLR='\n'
                inputLR1 = bytes(inputLR,encoding="utf8")
                fobj.write(inputLR1)
            allsrcid.add(srcid)
            input2 = srcid  + ' ' + dstid
            input21 = bytes(input2,encoding="utf8")
            fobj.write(input21)

    inputLR2 = '\n'
    inputLR21 = bytes(inputLR2, encoding="utf8")
    fobj.write(inputLR21)


f.close()
fobj.close()

