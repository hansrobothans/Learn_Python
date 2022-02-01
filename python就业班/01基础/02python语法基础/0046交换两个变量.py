# -*- coding:utf-8 -*-

a = 4
b = 5
a,b = b,a
print("a=",a)
print("b=",b)

a = a+b
b = a-b
a = a-b
print("a=",a)
print("b=",b)