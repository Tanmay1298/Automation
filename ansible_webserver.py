#!/usr/bin/python36
import subprocess as sp
import os

os.system("ansible all -m package -a 'name=httpd state=installed'")
os.system("ansible all -m service -a 'name=httpd state=restarted enabled=yes'")

