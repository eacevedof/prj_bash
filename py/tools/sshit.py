import sys
from getpass import getpass
import paramiko

# http://46.101.4.154/Art%C3%ADculos%20t%C3%A9cnicos/Python/Paramiko%20-%20Conexiones%20SSH%20y%20SFTP.pdf
class Sshit:

    shell = None
    dicaccess = None
    commands = []

    def __init__(self, dicaccess):
        print("Sshit: initializing...")
        self.dicaccess = dicaccess

    def connect(self):
        if self.dicaccess is None:
            print(f"Sshit: no acces data supplied")
            return None

        host = self.dicaccess["host"]

        self.shell = paramiko.SSHClient()
        self.shell.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            print(f"Sshit: ...trying to connect to {host}")
            self.shell.connect(self.dicaccess["host"],22,self.dicaccess["username"],self.dicaccess["password"])       
        except Exception as error:
            self.shell = None
            print(f"Sshit: not connected to host: {host}. error: {error}")


    def _cleanresponse(self,strrespose):
        strrespose = strrespose.decode()
        strclenaed = strrespose.replace("b'","").replace("\\\\n'","")
        return strclenaed

    def _print_cmd(self,indata,outdata,error):       
        #print(f"\nindata : {indata}")
        #print(f"\noutdata: {outdata.read()}")
        #print(f"\nerror: {error.read()}")
        cleaned = self._cleanresponse(outdata.read())
        print(f"Sshit: output: {cleaned}")
        cleaned = self._cleanresponse(error.read())
        if cleaned != "":
            print(f"Sshit: error: {cleaned}")

    def cmd(self, strcmd):
        self.commands.append(strcmd)

    def _get_unique_cmd(self):
        cmdunique = "; ".join(self.commands)
        return cmdunique

    def execute(self):
        if self.is_connected():
            shell = self.shell
            strcmd = self._get_unique_cmd()
            prcmd = strcmd.replace(";","\n\t")
            print(f"Sshit: cmd: {prcmd}")
            # shell.exec_command abre una instancia nueva por eso hay que contactenar los comandos
            indata, outdata, error = shell.exec_command(strcmd)
            self._print_cmd(indata,outdata,error)

    def close(self):
        if self.is_connected():
            host = self.dicaccess["host"]
            print(f"Sshit: clossing connection to: {host}")
            self.shell.close()

    def clear(self):
        self.commands = []

    def is_connected(self):
        return self.shell is not None            