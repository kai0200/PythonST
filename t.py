#!/usr/bin/env python
# encoding: utf-8

import socket

hostname = socket.gethostname()
print hostname.split('.')
