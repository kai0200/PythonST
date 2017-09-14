#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# textwrap_indent.py

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
for width in [45, 60]:
    print('{} Clumns:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()
