#!/usr/bin/env python
# encoding: utf-8

# string_template_advanced.py

import string

# delimiter 分符
# pattern 模式
class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]'


# underscore 下划线
template_text = '''
    Delimiter   :   %%
    Replaced    :   %with_underscore
    Ignored     :   %notunderscored
'''

#
d = {
    'with_underscore':   'relpaced',
    'notunderscored':   'not relpaced',
}


t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))

