#!/usr/bin/env python3
# encoding: utf-8

nums = [x for x in range(30) ]

for num in nums:
    print(num)

strs = [m + n for m in "ABC" for n in "XYZ"]
for str in strs:
    print(str)
