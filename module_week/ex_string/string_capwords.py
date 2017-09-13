#!/usr/bin/env python3
# encoding: utf-8
# string_capwords.py
# 20170912


import string

# capwords test
s = "The quick brown fox jumped over the lazy dog."

print(s)

print(string.capwords(s))

print('|'.join(s.split(' ')))

# format test
name = "Kevin"
age  = 18

s1 = "{someone}'s age is {howold}".format(someone=name, howold=age)
print(s1)

