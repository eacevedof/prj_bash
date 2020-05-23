import spur

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

        host = self.dicaccess["host"],
        shell = spur.SshShell(self.dicaccess["host"],self.dicaccess["username"],self.dicaccess["password"])
        if not shell:
            print(f"Sshit: not connected to host: {host}")
            return 0
        self.shell = shell
        print(f"Sshit: connected to host: {host}")

    def command(self,strcmd):
        if self.shell is None:
            print(f"Sshit: command {strcmd} not excecuted. Not connected to host")
            return 0
        
        with self.shell:
            result = self.shell.run(strcmd)
        print(result.output)

    def close(self):
        if self.shell is not None:
            pass
