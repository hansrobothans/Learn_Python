# -*- coding:utf-8 -*-

my_str = "hello world itcast and itcastxxxcpp"

print (my_str.find("world"))

print (my_str.find("haha"))

#从左边找
print (my_str.find("itcast"))

# 从右边找
print (my_str.rfind("itcast"))

# index
print (my_str.index("itcast"))

# rindex
print (my_str.rindex("itcast"))

# 抛出异常
print (my_str.index("haha"))
