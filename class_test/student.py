#!/usr/bin/env python
# encoding: utf-8

from  people import People

class Student(People):
    s_class = ''
    school_number = 0

    def __init__(self, n, a, w, c, s):
        People.__init__(self, n, a, w)
        self.s_class = c
        self.school_number = s

    def display_message(self):
        print "Class is %s, Number of school is %d" % (self.s_class, self.school_number)

s = Student('Tom', 18, 98, '0308', 2213)
s.speak()

s.display_message()

