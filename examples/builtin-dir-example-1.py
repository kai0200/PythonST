#!/usr/bin/env python
# encoding: utf-8

def dump(value):
    print value, '=>', dir(value)

import sys

dump(0)
dump(0.1)
dump([])
