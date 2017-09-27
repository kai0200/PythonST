#!/usr/bin/env python3
# encoding: utf-8

import collections

c = collections.Counter('extremely')
c['z'] = 0

print(c)
print(list(c.elements()))
