import sys
from getpass import getpass
import paramiko


# http://46.101.4.154/Art%C3%ADculos%20t%C3%A9cnicos/Python/Paramiko%20-%20Conexiones%20SSH%20y%20SFTP.pdf
class Sshit:
    shell = None
    dicaccess = None
    commands = []
    error = ""
    success = ""

    def __init__(self, dicaccess):
        print("Sshit: constructing...")
        self.commands = []
        self.error = ""
        self.success = ""
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
            self.shell.connect(self.dicaccess["host"], 22, self.dicaccess["username"], self.dicaccess["password"])
        except Exception as error:
            self.shell = None
            print(f"Sshit: not connected to host: {host}. error: {error}")

    @staticmethod
    def _cleanresponse(strrespose):
        strrespose = strrespose.decode()
        strclenaed = strrespose.replace("b'", "").replace("\\\\n'", "")
        strclenaed = strclenaed.strip()
        return strclenaed

    def _print_cmd_result(self, strcmd, success, error):
        # print(f"\nindata : {indata}")
        # print(f"\noutdata: {outdata.read()}")
        # print(f"\nerror: {error.read()}")
        print(f"\nstart===============================================")
        if error != "":
            print(f"Sshit cmd error:\n\t {strcmd}")
            print(f"\n{error}")
            print(f"end================================================\n")
            return

        print(f"Sshit result of:\n\t{strcmd}\n\n {success}")
        print(f"end================================================\n")

    def cmd(self, strcmd):
        self.commands.append(strcmd)

    def _get_unique_cmd(self):
        cmdunique = "; ".join(self.commands)
        return cmdunique

    def execute(self):
        if self.is_connected():
            shell = self.shell
            onelinecmd = self._get_unique_cmd()
            # shell.exec_command abre una instancia nueva por cmd. Este es el motivo de la contactenación con ; de los comandos
            indata, outdata, error = shell.exec_command(onelinecmd)
            self.error = self._cleanresponse(error.read())
            self.success = self._cleanresponse(outdata.read())
            self._print_cmd_result(onelinecmd, self.success, self.error)

    def close(self):
        if self.is_connected():
            host = self.dicaccess["host"]
            print(f"Sshit: clossing connection to: {host}")
            self.shell.close()

    def clear(self):
        self.success = ""
        self.error = ""
        self.commands = []

    def is_connected(self):
        return self.shell is not None

# end
