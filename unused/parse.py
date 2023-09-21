'''
Author: eive001 Yishang.Zhang@linux.alibaba.com
Date: 2023-03-28 01:11:14
LastEditors: eive001 Yishang.Zhang@linux.alibaba.com
LastEditTime: 2023-03-29 15:20:00
FilePath: /root/tools/CodeAnalyse/parse.py
Description: 

Copyright (c) 2023 by zhangyishang, All Rights Reserved. 
'''
# -*- coding: utf-8 -*-

import sys
import os

logname = str(sys.argv[1])
filename1 = str(sys.argv[2])  # 带有详细的调用参数
filename2 = str(sys.argv[3])  # 仅有函数名字  以及文件名字

print(logname   + "  :logname     ")
print(filename1 + "  :with  call information    ")
print(filename2 + "  :only FunctionName")

tag = 0
loglist = []
fun_stack_last = [["first", "second"]]

def parse_bt():
    global fun_stack_last
    global loglist
    del loglist[0]
    fun_stack = []

    for term in loglist:
        first_strip = term.split(" in ", 1)
        if len(first_strip) == 1:
            first_strip.append(first_strip[0])
        
        second_strip = first_strip[1].split(" at ", 1)
        if len(second_strip) == 1:
            second_strip.append(second_strip[0])
        
        third_strip = second_strip[1].split(" ")
        if second_strip[0][0] == '#':
            second_strip[0] = second_strip[0][4:]
        
        fun_stack.append([second_strip[0], third_strip[0]])
    
    loglist = []
    fun_stack.reverse()
    pos = min(len(fun_stack), len(fun_stack_last))
    for i in range(min(len(fun_stack), len(fun_stack_last))):
        if fun_stack[i] != fun_stack_last[i]:
            pos = i
            break
    
    while pos < len(fun_stack):
#        print((pos) * 2 * "  ", fun_stack[pos][0], " : ", fun_stack[pos][1])
        space = (pos) * 2 * " " 
        strout = "\" " +  space +  fun_stack[pos][0] + "   :   " + fun_stack[pos][1] + "\""
        os.system("echo "+   strout     + " >>"   + filename1)
        fun_name = fun_stack[pos][0].split("(")
        strout = "\" " +  space +  fun_name[0] + "()   :   " + fun_stack[pos][1] + "\""
        os.system("echo "+ strout + "  >>  " + filename2)
        pos += 1
    fun_stack_last = fun_stack

with open(logname, 'r') as f:
    for line in f:
        if tag == 0:
            if len(line.strip()) == 0:
                tag = 1
        elif tag == 1 or tag == 2:
            if tag == 1:
                if line.find(" main ") != -1:
                    tag = 2
                    loglist = []
            elif tag == 2:
                if line.find("__do_global_dtors_aux") != -1:
                    exit()
            
            if len(line.strip()) == 0 and tag == 2:
                parse_bt()
            elif line[0] != 'B' and line[0] != '#':
                #loglist[-1] = loglist[-1] + " " + line[:-1]
                continue
            else: 
                loglist.append(line[:-1])
        else:
            exit()
