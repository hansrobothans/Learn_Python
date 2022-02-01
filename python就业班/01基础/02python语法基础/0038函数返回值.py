# -*- coding:utf-8 -*-

def test():
    a = 11
    b = 22
    c = 33

    # 第一种，用一个列表来封装3个变量的值
    # d = [a,b,c]
    # return d

    # 第二种
    # return [a,b,c]

    # 第三种
    # return (a,b,c)

    return a,b,c

# 有多个返回值的函数
print(test())
