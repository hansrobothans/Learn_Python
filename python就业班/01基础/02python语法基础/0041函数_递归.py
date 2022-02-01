# -*- coding:utf-8 -*-

#求阶乘
"""
i = 1
result = 1
while i<=4:
    result = result * i
    i+=1

print("4!=%d"%(result))
"""
def get_num(num):
    if num>1:
        return num * get_num(num-1)
    else:
        return num
        
print(get_num(4),end="")



