#!/usr/bin/env python
# encoding: utf-8

class Computer(object):
    cpu = ''
    mem = 0
    __ipaddress = ''

    def __init__(self, c, m, i):
        self.cpu = c
        self.mem = m
        self.__ipaddress = i

    def display_message(self):
        print "Computer cpu is %s, Mem are %dG" % (self.cpu, self.mem)

if __name__ == "__main__":
    ibm = Computer("Inter", 160, "192.168.160.63")
    ibm.display_message()

