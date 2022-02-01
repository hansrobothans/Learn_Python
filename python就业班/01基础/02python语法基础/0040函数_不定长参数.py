# -*- coding:utf-8 -*-

def sum_1_nums(a,b,*args):
    "不定长参数。args可以起其他名字"
    print(a)
    print(b)
    print(args)

# 不定长参数函数
sum_1_nums(11,22,33,44,55,66,77,88)
sum_1_nums(11,22)
# sum_1_nums(11)#错误，因为 形参中 至少要有俩实参

def sum_2_nums(a,b,c=33,*args):
    "不定长参数和缺省参数。args可以起其他名字"
    print(a)
    print(b)
    print(c)
    print(args)

# 不定长——缺省参数函数
sum_2_nums(11,22,33,44,55,66,77,88)


def sum_3_nums(a,b,c=33,*args,**kwargs):
    "不定长参数和缺省参数。args可以起其他名字"
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

# 不定长——缺省参数函数
sum_3_nums(11,22,33,44,55,66,done=77,task=88)