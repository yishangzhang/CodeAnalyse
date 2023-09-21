/*
 * @Author: eive001 Yishang.Zhang@linux.alibaba.com
 * @Date: 2023-03-28 01:26:41
 * @LastEditors: eive001 Yishang.Zhang@linux.alibaba.com
 * @LastEditTime: 2023-03-29 15:20:30
 * @FilePath: /root/tools/CodeAnalyse/test.cpp
 * @Description: 
 * 
 * Copyright (c) 2023 by zhangyishang, All Rights Reserved. 
 */


#include<iostream>

using namespace std;

void fun1(int x)
{
    x = x*x;

    cout<<x<<endl;
}


void fun2(int y)
{
    y = y+y;

    cout<<y<<endl;

}


int main()
{

int a = 9;
int b  =6;

fun1(a);

fun2(b);

}