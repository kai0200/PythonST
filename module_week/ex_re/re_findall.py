#!/usr/bin/env python
# encoding: utf-8

import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for matche in re.findall(pattern, text):
    print('Found {!r}'.format(matche))
