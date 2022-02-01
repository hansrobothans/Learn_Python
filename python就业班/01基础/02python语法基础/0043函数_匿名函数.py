# -*- coding:utf-8 -*-

# nums = [11,22,55,1,5,88,228,98,2]
# nums.sort()
# print(nums)

infors = [
    {"name":"laowang","age":10},
    {"name":"laozhao","age":80},
    {"name":"laoli","age":70},
    {"name":"laozhang","age":110},
    ]
infors.sort(key=lambda x:x["name"])
print(infors)
