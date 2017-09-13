# encoding: utf-8
# textwrap_dedent.py

# dedent 取消缩进

import textwrap
from textwrap_example import sample_text


dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
