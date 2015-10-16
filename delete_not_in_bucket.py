#!/usr/bin/env python
# encoding: utf-8

import os
import socket

# shell find 所有用户的目录
def find_userdir():
    return os.system("find /maildata/[0-f] -maxdepth 4 -mindepth 4 > /tmp/userDir.txt")

#  def find_userdir():
    #  for root, d, f in os.walk("/tmp/maildata"):
        #  dirpath_split = root.split('/')
        #  if len(dirpath_split) == 7:
            #  #  and\
                #  #  dirpath_split[6] == 'deleted' and\
                #  #  len(dirpath_split[2]) == 1:
            #  print root
            #  print '*' * 20

# 获取桶的域名sohu.com chinaren.com sogou.com 17173.com
def get_bucket_host():

    hostname = socket.gethostname()
    return hostname


# 定义获取用户所在桶的函数
def get_user(hostname, port, user, domain):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))
    sock.send("get %s@%s\n" % (user, domain))
    rec = sock.recv(300)
    return rec


# 检查用户是否是本桶用户
# 0 1:11:/1/17/1/user1101:996457525:1422428016:user1101_new::chinaren5:1.0:1976-01-01|1|1|1000|1|1::::::::
def del_user(userDir):
    pass


if __name__ == "__main__":
    # 主循环判断用户不在桶删除用户的目录
    print "Main...."
    find_userdir()

    # test part

    import os



