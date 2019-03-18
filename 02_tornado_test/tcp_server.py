#!/usr/bin/env python
# encoding: utf-8

from tornado import ioloop, httpclient, gen
from tornado.gen import Task
#from tornado.tcpserver import TCPServer
try:
        from tornado.netutil import TCPServer
except:
        from tornado.tcpserver import TCPServer

import pdb, time, logging
from tornado import stack_context
from tornado.escape import native_str

#Init logging
def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s')
    sh.setFormatter(formatter)

    logger.addHandler(sh)
    logging.info("Current log level is : %s", logging.getLevelName(logger.getEffectiveLevel()))

class MyServer(TCPServer):
    def __init__(self, io_loop=None, **kwargs):
        TCPServer.__init__(self, io_loop=io_loop, **kwargs)

    def handle_stream(self, stream, address):
        TCPConnection(stream, address, io_loop=self.io_loop)

    def _on_timeout(self):
        logging.info("Send message..")
        self.write("Hello client!" + self.EOF)

    def _on_message(self, data):
        try:
            timeout = 5
            data = native_str(data.decode('latin1'))
            logging.info("Received: %s", data)
            self.io_loop.add_timeout(self.io_loop.time() + timeout, self._on_timeout)
        except Exception, ex:
            logging.error("Exception: %s", str(ex))


