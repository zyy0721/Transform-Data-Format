#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/3/13 21:21
#!@Author : zyy
#!@File   : DataTransforGiraph.py

print("hello,world")


#filename='D:\Datasets\\test.txt'
#fileNew = 'D:\Datasets\\testNew.txt'
filename='D:\Datasets\com-friendster.ungraph\com-friendster.ungraph.txt'
fileNew = 'D:\Datasets\com-friendster.ungraphNew.txt'

allsrcid=set('')
print(allsrcid)
fobj = open(fileNew, 'w+')
with open(filename,'r') as f:
    next(f)
    next(f)
    next(f)
    next(f)
    #skip first four lines
    count = 0
    for line in f:
        count +=1
        line = line.replace('\n', '')  # 去掉换行符，需要注意
        print(line)
        res = line.split()
        srcid = res[0]
        dstid = res[1]
        if srcid in allsrcid:
            #如果不是新的srcId，拿到destid 并设置value 为1，
            fobj.write(','+'[' + dstid + ',' + '1' + ']')
        else:
            #如果是一个新的srcId，判断是不是第一个，如果不是，就需要把之前的一行结束，如果是照常，加入set中，并且value初始值为0，然后接着把destid与value加入
            if allsrcid.__len__() != 0:
                fobj.write(']'+']'+'\n')
            allsrcid.add(srcid)
            fobj.write('[' + srcid + ',' + '0' + ','+'[' +'[' + dstid+ ',' + '1'+ ']')
        if count == 1806067135:
            print("last one")
            fobj.write(']' + ']' + '\n')

f.close()
fobj.close()
