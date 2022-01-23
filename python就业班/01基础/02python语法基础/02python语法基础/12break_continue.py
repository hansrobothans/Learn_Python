# -*- coding:utf-8 -*-

#输入 
name = input("请输入你的名字：")

print("下面依次输出你的名字每个字：")
print('不输出张')
print('遇到G停止输出')
#开始循环
for i in name:
    if i=='G':
        break
    if i=='张':
        continue
    print(i)






    






