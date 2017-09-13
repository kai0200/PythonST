#!/usr/bin/env python
# encoding=utf8


import sys
import random

# 拆分字符串爲單個字符，拆分字符串为单个字符

thestring = "abcdefg"

# Way  1
the_list = list(thestring)
print the_list

# Way 2
for c in thestring:
    print c

# Way 3
results = [c for c in thestring]

print results.append('3')
print results

# Way 4
results = map(ord, thestring)
print results
