#!/usr/bin/env python3
# encoding: utf-8

import enum

class BugStatus(enum.Enum):
    """
    Bug 状态
    """

    new = 7
    incomplete = 6   #残缺
    invalid = 5      #无效
    wont_fix = 4
    in_progress = 3
    fix_committed = 2  # 提交
    fix_released = 1   # 发布

    by_design = 4
    closed = 1


for status in BugStatus:
    """
    重名枚举member 不出现在name里
    """
    print('{:15} = {}'.format(status.name, status.value))

print('\nSame: by_design is wont_fix: ',
      BugStatus.by_design is BugStatus.wont_fix)
print('Same: closed is fix_released: ',
      BugStatus.closed is BugStatus.fix_released)
