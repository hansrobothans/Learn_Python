# -*- coding:utf-8 -*-

# 常用的数据类型转换
# 函数	说明
# int(x [,base ])	        将x转换为一个整数
# long(x [,base ])	        将x转换为一个长整数
# float(x )	                将x转换到一个浮点数
# complex(real [,imag ])	创建一个复数
# str(x )	                将对象 x 转换为字符串
# repr(x )	                将对象 x 转换为表达式字符串
# eval(str )	            用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s )	                将序列 s 转换为一个元组
# list(s )	                将序列 s 转换为一个列表
# chr(x )	                将一个整数转换为一个字符
# unichr(x )	            将一个整数转换为Unicode字符
# ord(x )	                将一个字符转换为它的整数值
# hex(x )	                将一个整数转换为一个十六进制字符串
# oct(x )	                将一个整数转换为一个八进制字符串

a = '1'
b = 51
c = '10+20'


print('======================================================')
print(a)
print('a的类型:',type(a))

print("a=int(a):%d"%(int(a)))

#在实际测试python3中，没有long转换
#print("a=long(a):%d"%(long(a)))

print("a=float(a):%f"%(float(a)))

# 复数
# aa=123-12j
# print aa.real  # output 实数部分 123.0  
# print aa.imag  # output虚数部分 -12.0
print("a=complex(a):",complex(a))

print("a=ord(a):%d"%(ord(a)))

print('======================================================')
print(b)
print('b的类型:',type(b))

print("b=str(b):%s"%(str(b)))

#chr即数转换成ascii
print("b=chr(b):%s"%(chr(b)))

#在实际测试python3中，没有unichr转换
# print("b=unichr(b):%s"%(unichr(b)))


print('======================================================')
print(c)
print('c的类型:',type(c))
#repr没太明白
print('c=repr(x):',repr(c))










