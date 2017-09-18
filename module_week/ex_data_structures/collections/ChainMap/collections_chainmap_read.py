#!/usr/bin/env python3
# encoding: utf-8

import collections
"""
collections  集合
"""

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D', 'e': 'E'}

m = collections.ChainMap(a, b) # 合并两个字典 D 被删除了

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print()

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))
