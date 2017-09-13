#!/usr/bin/env python
# encoding: utf-8

class People(object):
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n="", a=0, w=0):
        self.name = n
        self.age  = a
        self.__weight = w

    def speak(self):
        print("%s is speaking: I am %d years old" % (self.name, self.age))

if __name__ == '__main__':
    p = People('Tom', 36, 98)
    p.speak()
