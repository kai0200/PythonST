#!/usr/bin/env python3
# encoding: utf-8

# enum_unique_enforce.py

import enum

@enum.unique  # unique 修饰器保证 enum 唯一
class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    # This will trigger an error with unique applied.
    by_design = 4
    closed = 1
