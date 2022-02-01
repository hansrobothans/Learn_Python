# -*- coding:utf-8 -*-

def test(a,b,func):
    return func(a,b)

# 获取键盘输入
fun_new = input("请输入一个匿名函数:")
fun_new = eval(fun_new)
num = test(11,22,fun_new)
print(num)
