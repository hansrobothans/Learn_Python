# -*- coding:utf-8 -*-

laowang = {"name":"班长"}
print(laowang)

# 当没有键的时候，相当于增加
laowang['qq'] = 10010
print(laowang)

# 当有键的时候，是修改
laowang['qq'] = 10086
print(laowang)

# pop(key[,default])
# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
laowang.pop("name")
print(laowang)





