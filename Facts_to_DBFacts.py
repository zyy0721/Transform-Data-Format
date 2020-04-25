# ！/usr/bin/env python
# !-*-coding:utf-8 -*-

filename = 'F:\\NJU\\Datasets\\DBDatalog\\tree11.facts'
fileNew = 'F:\\NJU\\Datasets\\DBDatalog\\tree11_dbd.facts'

fobj = open(fileNew, 'wb+')
with open(filename,'r') as f:
    for line in f:
        line = line.replace('\n', '')  # 去掉换行符，需要注意
        print(line)
        res = line.split('\t')
        srcid = res[0]
        dstid = res[1]
        input = srcid + ',' + dstid + ',' + '\n'
        input1 = bytes(input, encoding="utf8")
        fobj.write(input1)





f.close()
fobj.close()
print("Finished!")