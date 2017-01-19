#!/usr/bin/env python
# encoding: utf-8

import sys, os, htmllib, formatter

#使用unix 的tput
set_bold = os.popen('tput bold').read()
set_underline = os.popen('tput smul').read()
perform_reset = os.popen('tput sgr0').read()

class TtyFormatter(formatter.AbstractFormatter):
    ''' 一个保留粗体和斜体状态的格式化对象，并输出相应的终端控制队列'''
    def __init__(self, writer):
        formatter.AbstractFormatter.__init__(self, writer)
        # 开始没有粗体也没有斜体
        self.fontState = False, False
        self.fontStack = [ ]
    def push_font(self, font):
        # 我们之关注粗体和斜体
        size, is_italic, is_bold, is_tt = font
        self.fontStack.append((is_italic, is_bold))
        self._updateFontState()
    def pop_font(self, *args):
        # 回到前一个font状态
        try:
            self.fontStack.pop()
        except IndexError:
            pass
        self._updateFontState()
    def updateFontState(self):
        try:
            newState = self.fontStack[-1]
        except IndexError:
            newState = False, False
        if self.fontState != newState:
            #相关的状态改变重置终端
            print perform_reset,
            #如果需要的话，设置下划线与/或粗体状态
            if newState[0]:
                print set_underline,
            if newState[1]:
                print set_bold,
            #记住当前两个状态
            self.fontStack = newState

# 生成写入、格式化、解析对象、根据需要将它们连接起来
myWriter = formatter.DumbWriter()
if sys.stdout.isatty():
    myFormatter = TtyFormatter(myWriter)
else:
    myFormatter = formatter.AbstractFormatter(myWriter)
myParser = htmllib.HTMLParser(myFormatter)
# 将标准输入和终端操作提供给解析器  此处调试没有通过需要再看一下
myParser.feed(sys.stdin.read)
myParser.close()
