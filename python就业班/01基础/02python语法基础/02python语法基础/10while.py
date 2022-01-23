# -*- coding:utf-8 -*-

#输入 
begin = input("请输入累加开始的数:")
end = input("请输入累加结束的数:")

#转换类型
begin_num = int(begin)
end_num = int(end)
sum =begin_num

#开始累加
while begin_num < end_num:
    begin_num +=1
    # print("begin_num:%d"%begin_num)
    sum += begin_num

#输出累加结果
print("累加结果：%d"%sum)


    






