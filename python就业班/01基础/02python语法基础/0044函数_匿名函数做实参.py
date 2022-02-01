# -*- coding:utf-8 -*-

def test(a,b,func):
    return func(a,b)

num = test(11,22,lambda x,y:x+y)
print(num)
