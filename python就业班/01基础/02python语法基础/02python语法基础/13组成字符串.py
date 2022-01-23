# -*- coding:utf-8 -*-

a = 'haha'

# 通过格式控制符组成字符串，当后面有变量当作格式控制符，否则当成普通的字符
b = '%sworld'%(a)
print(b)

c = '%sworld'
print(c)

#要么不提供，要么提供全
# d = '%sworld%s'%(a)
d = '%sworld%s'%(a,a)
print(d)
