#!/usr/bin/env python3
# encoding: utf-8

import re

text = 'This is some text -- with punctuation.'
pattern = re.compile(r'\b\w*is\w*\b')

print('Text',text)
print()

pos = 0
while True:
    match = pattern.search(text, pos)
    if not match:
        break
    s = match.start()
    e = match.end()
    print(' {:>2d} : {:>2d} = "{}"'.format( # > 右对齐 2 两位: 表示数字
        s, e - 1, text[s:e]))
    pos = e
