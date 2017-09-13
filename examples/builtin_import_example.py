#!/usr/bin/env python
# encoding: utf-8

import glob,os

modules = []

for module_file in glob.glob("*-plugin.py"):
    try:
        print module_file
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        module = __import__(module_name)
        modules.append(module)
    except ImportError, e:
        print e

for module in modules:
    module.hello()
