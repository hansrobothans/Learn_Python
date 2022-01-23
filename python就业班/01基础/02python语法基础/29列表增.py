# -*- coding:utf-8 -*-
names1 = ['laowang','laoli','laoliu']

print(names1)

# 添加,添加到最后
names1.append('laozhao')
print(names1)

names1.append('wukong')
print(names1)

#添加，第一个参数指定添加位置
names1.insert(0,'bajie')
print(names1)

names2 = ['老王','老李','老刘']

names3 = names1 + names2
print(names3)

#names2后面扩充names1
names2.extend(names1)
print(names2)





