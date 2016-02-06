# -*- coding: utf-8 -*-
from musicPlayer import musicPlayer
from newsStation import newsparser
from yukkuri import yukkuri
from mail import mail
import socket
import subprocess

buf = subprocess.call("python newsStation/call.py",shell=True)
