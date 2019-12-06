#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time
import itertools
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
from fabric.contrib.files import *
from time import *

# 配置角色信息
env.user = 'root'
env.password = '123456'

env.roledefs = {
     'role01': ['192.168.37.94'],
     'role02': ['192.168.37.102'],
     'role03': ['192.168.37.105'],
     'role04': ['192.168.37.103'],
     'role05': ['192.168.37.104'],
     'all': ['192.168.37.105','192.168.37.102','192.168.37.94','192.168.37.103','192.168.37.104'],
     }

def choose():
  print red("==============================================================================================================")
  print yellow("up_nginx    ")+blue("nginx核心配置管理 ")+white("nginx配置更新")+yellow("请输入下列")
  print red("==============================================================================================================")
  iterms=sorted(list(env.roledefs));
  counts=len(iterms);
  for i in reversed(range(0,counts)):
    if( i < 100 ):
      j="%3s"%i
    else:
      j=i
    print "     [\033[1;47;46m",j,"\033[0m]",'----->',iterms[i];
  print red("==============================================================================================================")
  select_id = int(raw_input("请选择代理ID: "))
  global servers,conf_dir
  servers=iterms[select_id]
  print (servers)

choose()


@roles(servers)
def up_nginx():
    run('/usr/local/nginx/sbin/nginx -t')
    run('/usr/local/nginx/sbin/nginx -s reload')
#    test()
#
#def test():
#    run('echo  file01')
