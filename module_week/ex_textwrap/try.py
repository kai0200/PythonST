#!/usr/bin/env python3

import textwrap
import re

from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
print(dedented_text)


pattern = 'The'
match = re.search(pattern, sample_text)
s = match.start()
e = match.end()

print("pattern:{} Start: {} End: {}".format(pattern, s, e))
