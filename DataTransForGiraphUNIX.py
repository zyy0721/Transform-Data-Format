#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/3/25 18:47
#!@Author : zyy
#!@File   : DataTransForGiraphUNIX.py

print("hello,world")


#filename='D:\Datasets\\test.txt'
#fileNew = 'D:\Datasets\\testNewUNIX.txt'
filename='D:\Datasets\web-Google\web-Google.txt'
fileNew = 'D:\Datasets\web-GoogleNewUnix.txt'

allsrcid=set('')
print(allsrcid)
with open(filename,'r') as f:
    next(f)
    next(f)
    next(f)
    next(f)
    #skip first four lines
    lines = f.readlines()
    last_line = lines[-1]
    last_line = last_line.replace('\n','')
    fobj = open(fileNew,'wb+')
    for line in lines:
        line = line.replace('\n','')#去掉换行符，需要注意
        print(line)


        res = line.split()
        srcid = res[0]
        dstid = res[1]
        if srcid in allsrcid:
            #如果不是新的srcId，拿到destid 并设置value 为1，
            input = ','+'[' + dstid + ',' + '1' + ']'
            input1 = bytes(input,encoding="utf8")
            fobj.write(input1)
        else:
            #如果是一个新的srcId，判断是不是第一个，如果不是，就需要把之前的一行结束，如果是照常，加入set中，并且value初始值为0，然后接着把destid与value加入
            if allsrcid.__len__() != 0:
                input2 = ']'+']'+'\n'
                input21 = bytes(input2,encoding="utf8")
                fobj.write(input21)
            allsrcid.add(srcid)
            input3 = '[' + srcid + ',' + '0' + ','+'[' +'[' + dstid+ ',' + '1'+ ']'
            input31 = bytes(input3,encoding="utf8")
            fobj.write(input31)

        if line == last_line:
            input2 = ']' + ']' + '\n'
            input21 = bytes(input2, encoding="utf8")
            fobj.write(input21)


f.close()
fobj.close()
