#!/usr/bin/env python
# encoding=utf8
import random

c = "1231fdsadsfcvvxzcx6543hgdmhfg76865kjgg"

s = ""
for i in range(1, 10):
    s = s + random.choice(c)

print s
