# -*- coding:utf-8 -*-

names1 = ['laowang','laoli','laoliu','老王','老李','老刘']

# pop：删除最后一个元素
names1.pop()
print(names1)

# remove：根据内容进行删除且从左往右只删除一次 
names1.remove("laoli")
print(names1)

##### del：根据下标进行删除
del names1[2]
print(names1)








