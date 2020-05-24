import sys
from getpass import getpass
import paramiko

# http://46.101.4.154/Art%C3%ADculos%20t%C3%A9cnicos/Python/Paramiko%20-%20Conexiones%20SSH%20y%20SFTP.pdf
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

    def _print_cmd(self,indata,outdata,error):
        print(f"\nindata : {indata}")
        print(f"\noutdata: {outdata}")
        print(f"\nerror: {error}")

    def command(self,strcmd):
        shell = self.shell
        indata, outdata, error = shell.exec_command(strcmd)
        self._print_cmd(indata,outdata,error)
        #print(outdata.read())
        # self.close()

    def close(self):
        host = self.dicaccess["host"]
        print(f"clossing connection to: {host}")
        self.shell.close()