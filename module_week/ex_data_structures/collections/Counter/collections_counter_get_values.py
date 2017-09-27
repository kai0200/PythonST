#!/usr/bin/env python3
# encoding: utf-8

import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))
