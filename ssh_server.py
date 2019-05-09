#!/usr/bin/python36
import os
import subprocess
import getpass

ip = input("Enter IP")

os.system("ssh {} 'yum install openssh-server -y'".format(ip))
