#!/usr/bin/env python
# encoding: utf-8

# string_template.py

import string

values = {'var': 'foo'}

# Test "${}"
t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))


# Test "%()"
s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable

"""

print('INTERPOLATION:', s % values)


# Test "{}"
s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}siable

"""

print('FORMAT:', s.format(**values))
