# -*- coding:utf-8 -*-

num = input("请输入一个选项（1-6）")


if num.isalpha():
    print("输入的字母")

if num.isdigit():
    print("是数字")

if num.isalnum():
    print("是数字或字母")
