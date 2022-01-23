# -*- coding:utf-8 -*-

name = 'abcdefABCDEF'

# abcdefABCDEF
print(name[0:])

# F
print(name[-1:])

# 
print(name[-1:0])

# FEDCBAfedcb
print(name[-1:0:-1])

# FEDCBAfedcba
print(name[-1::-1])

# FEDCBAfedcba
print(name[::-1])