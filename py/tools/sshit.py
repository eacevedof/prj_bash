import os
import sys
from pexpect import pxssh
import getpass from getpass

class Sshit:

    objserv = None
    dicaccess = None

    def __init__(self, dicaccess):
        print("Sshit: initializing...")
        self.dicaccess = dicaccess

    def connect(self):
        if self.dicaccess is None:
            print(f"Sshit: no acces data supplied")
            return 0

        s = pxssh.pxssh()
        host = self.dicaccess["host"],
        is_logged = s.login(self.dicaccess["host"],self.dicaccess["username"],self.dicaccess["password"]):
        if not is_logged:
            print(f"Sshit: not connected to host: {host}")
            return 0
        self.objserv = s
        print(f"Sshit: connected to host: {host}")

    def command(self,strcmd):
        if self.objserv is None:
            print(f"Sshit: command {strcmd} not excecuted. Not connected to host")
            return 0
        objserv = self.objserv
        child = objserv.spawn(strcmd,encoding="utf-8")
        child.logfile = sys.stdout
        # objserv.sendline(strcmd)

    def close(self):
        if self.objserv is not None:
            self.objserv.logout()
