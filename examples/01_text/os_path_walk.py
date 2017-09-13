#!/usr/bin/env python
# encoding: utf-8

import os, os.path

def visit_dir(arg, dirname, names):
    print "%s, arg = %s" % (type(arg), arg)
    print "%s, dirname = %s" % (type(dirname), dirname)
    print "%s, name = %s" % (type(names), names)
    print
    for filespath in names:
        print os.path.join(dirname, filespath)

    print "-" * 20

if __name__ == '__main__':
    path = '/tmp/maildata'
    os.path.walk(path, visit_dir,('chi'))
