#!/usr/bin/env python3
# encoding: utf-8

#Author: Kevin.W.K
#Email: kai0200@gmail.com
#Date: 2017-09-17
#Desc: Dissecting Matches with Groups 用组解析匹配

from re_test_patterns import test_patterns

test_patterns(
        'abbaaabbbbaaaaa',
        [
         ('a(ab)',   'a followed by literal ab'),      #字母a后面跟着ab
         ('a(a*b*)', 'a followed by 0-n a and 0-n b'), #a 后面跟着0-n个a 和 n个b
         ('a(ab)*',  'a followed by 0-n ab'),
         ('a(ab)+',  'a followed by 1-n ab')           # 1-n 个 + 号的意义
        ],
)
