#!/usr/bin/env python3
# encoding: utf-8

import difflib

from difflib_data import *

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))
