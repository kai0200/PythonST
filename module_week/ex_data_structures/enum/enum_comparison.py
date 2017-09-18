#!/usr/bin/env python3
# encoding: utf-8

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


actual_state = BugStatus.wont_fix  #actual_state  当前状态
desired_state = BugStatus.fix_released    # desired_state  期望状态

print('Equality:',
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)
print('Identity:',
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)
print('Ordered by value:')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus))) # enum.Enum 不支持sort
except TypeError as err:
    print('  Cannot sort: {}'.format(err))
