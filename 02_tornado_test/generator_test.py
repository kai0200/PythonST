#!/usr/bin/env python
# encoding: utf-8

import pdb

S = ['EMPTY']

def gen():
    for i in ['a', 'b']:
        print i
    for i in range[10]:
        S[0] = yield i
        print str(S[0])

g = gen()

pdb.set_trace()
print g.next()
pdb.set_trace()
print g.send('ok')
print g.next()
