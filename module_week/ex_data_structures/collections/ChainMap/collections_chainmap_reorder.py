#!/usr/bin/env python3
# encoding: utf-8

# Reordering  集重新排序

import collections
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print(m.maps)
print('c = {}\n'.format(m['c']))

# reverse the list 反向
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))
