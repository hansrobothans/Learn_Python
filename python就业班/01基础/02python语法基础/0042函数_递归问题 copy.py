# -*- coding:utf-8 -*-

#求阶乘
def get_num(num):
    if num>1:
        return num * get_num(num-1)
    else:
        return num
        
print(get_num(4),end="")



