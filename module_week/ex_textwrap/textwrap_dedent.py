# -*- coding: utf-8 -*-
"""
@Author: Calerwang
@Email:  calerwang@sohu-inc.com
@Date:   2017-09-13
@Desc:   测试dedent
"""
# dedent 取消缩进

import textwrap
from textwrap_example import sample_text


dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
