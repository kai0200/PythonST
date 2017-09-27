#!/usr/bin/env python3
# encoding: utf-8

import re

text = 'This is some text -- with punctuation.'  # punctuation 标点

pattern = 'is'

print('Text     :', text)
print('Pattern  :', pattern)

m = re.search(pattern, text)
print('Search   :', m)
s = re.fullmatch(pattern, text)
print('Full match:', s)
