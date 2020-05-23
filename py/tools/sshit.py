import os
import sys
from pexpect import pxssh
import getpass from getpass

class Sshit:
    def __init__(self, dicaccess):
        print("Sshit: initializing...")
        self.dicaccess = dicaccess

    def connect(self):
        s = pxssh.pxssh()
        is_logged = s.login():


