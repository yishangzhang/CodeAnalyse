'''
Author: eive001 Yishang.Zhang@linux.alibaba.com
Date: 2023-03-28 01:10:43
LastEditors: eive001 Yishang.Zhang@linux.alibaba.com
LastEditTime: 2023-03-29 15:21:48
FilePath: /root/tools/CodeAnalyse/debug.in.py
Description: 

Copyright (c) 2023 by zhangyishang, All Rights Reserved. 
'''

# -*- coding: utf-8 -*-

import os
gdb.execute("set logging on")
gdb.execute("set height 0")

f = open("map", 'r')
for line in f:
	gdb.execute("b " + line[19:len(line)-1]);
f.close()

#gdb.execute(str(sys.argv[1]));

gdb.execute("run _replace_  > /dev/null");
while 1:
	gdb.execute("bt");
	gdb.execute("c");

