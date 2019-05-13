#！/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Create :2019/4/17 16:17
#!@Author : zyy
#!@File   : DataTransforSouffleSpnode.py



filename='D:\Datasets\wiki-Talk\WikiTalk.txt'
fileNew1 = 'D:\Datasets\Souffle\\node.facts'
fileNew2 = 'D:\Datasets\Souffle\\num_node.facts'
allnode=set('')
#filename='D:\Datasets\wiki-Talk\WikiTalk.txt'
#fileNew = 'D:\Datasets\Souffle\\wikiedgesp.facts'
fobj1 = open(fileNew1, 'wb+')
fobj2 = open(fileNew2, 'wb+')
with open(filename,'r') as f:
    next(f)
    next(f)
    next(f)
    next(f)
    #skip first four lines
    for line in f:
        line = line.replace('\n', '')  # 去掉换行符，需要注意
        res = line.split()
        srcid = res[0]
        dstid = res[1]
        print("srcid is : " + srcid + "  dstid is :  " + dstid)
        if srcid not in allnode:
            allnode.add(srcid)
            linesrc = str(srcid) + '\n'
            print(linesrc)
            wrlinesrc = bytes(linesrc,encoding="utf8")
            fobj1.write(wrlinesrc)
            fobj2.write(wrlinesrc)
        if dstid not in allnode:
            allnode.add(dstid)
            linedst = str(dstid) + '\n'
            print(linedst)
            wrlinedst = bytes(linedst, encoding="utf8")
            fobj1.write(wrlinedst)
            fobj2.write(wrlinedst)



f.close()
fobj1.close()
fobj2.close()
print("Finished!")