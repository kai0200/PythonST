#!/usr/bin/env python
# encoding: utf-8

#对文件名和文件对象使用 type 函数

def load(file):
    if isinstance(file, type("")):
        file = open(file, 'rb')

    return file.read()

print len(load("samples/sample.jpg")), "bytes"
print len(load(open("samples/sample.jpg", 'rb'))), "bytes"
