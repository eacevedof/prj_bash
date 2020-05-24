import sys
from getpass import getpass
import paramiko

class Sshit:

    shell = None
    dicaccess = None

    def __init__(self, dicaccess):
        print("Sshit: initializing...")
        self.dicaccess = dicaccess

    def connect(self):
        if self.dicaccess is None:
            print(f"Sshit: no acces data supplied")
            return 0

        host = self.dicaccess["host"]

        self.shell = paramiko.SSHClient()
        # print(self.shell); sys.exit()

        #if "sshkey" in self.dicaccess.keys():
        self.shell.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.shell.connect(self.dicaccess["host"],22,self.dicaccess["username"],self.dicaccess["password"])

        if not self.shell:
            print(f"Sshit: not connected to host: {host}")
            return 0
        #print(f"Sshit: connected to host: {host}")
        return self.shell

    def command(self,strcmd):
        shell = self.shell
        indata, outdata, error = shell.exec_command(strcmd)
        print(outdata.read())
        # self.close()

    def close(self):
        self.shell.close()