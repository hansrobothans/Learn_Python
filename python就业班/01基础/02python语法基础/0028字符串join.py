# -*- coding:utf-8 -*-

a = ["aaa","bbb","cccc"]

b = "="
print(b.join(a))
# aaa=bbb=cccc

b = " "
print(b.join(a))
# aaa bbb cccc

b = ""
print(b.join(a))
# aaabbbcccc

b = "hello word"
print(b.join(a))
# aaahello wordbbbhello wordcccc

b = "hello word"
print(b.join("aaa"))
# ahello wordahello worda
