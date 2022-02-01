# -*- coding:utf-8 -*-

a = (11,22)
b = a
print(b)

#相当于拆包
c,d = a
print(c)
print(d)


a = (11,22,33)

#会报错，必须等号左右两边能一一对应
c,d= a
print(c)
print(d)