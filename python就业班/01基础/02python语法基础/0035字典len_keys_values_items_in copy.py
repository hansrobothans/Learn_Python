# -*- coding:utf-8 -*-

laowang = {"name":"班长","addr":"山东","age":18}

# 测量字典中，键值对的个数
print(len(laowang))

# 返回一个包含字典所有KEY的视图对象
# dict_keys = laowang.keys()
# print(dict_keys)
print(laowang.keys())

# 返回一个包含字典所有value的视图对象
print(laowang.values())

# 返回一个包含所有（键，值）视图对象
print(laowang.items())

#has_key在python3中被取消了
# dict.has_key(key)如果key在字典中，返回True，否则返回False
# print(laowang.has_key("班长"))

#in ，not in
# print("班长" in laowang)
print("name" in laowang)



