import pysftp
import sys
import os

# https://stackoverflow.com/questions/432385/sftp-in-python-platform-independent
class Sftp:
    objserver = None

    def __init__(self, dicaccess):
        print("Sftp: initializing...")
        self.dicaccess = dicaccess

    def connect(self):
        print("Sftp: trying to connect...")
        config = self.dicaccess
        host = config["host"]
        username = config["username"]
        password = config["password"]
        port = config["port"] if "port" in config.keys() else 22 # entero
        #print(config);sys.exit()
        try:
            # self.objserver = pysftp.Connection(host=host, username=user, password=password, port=port)
            self.objserver = pysftp.Connection(host=host, username=username, password=password)
            print(f"Sftp: connected to host: {host}")
        except Exception as error:
            print(f"Sftp: error trying to connect to {host} error: {error}")

    def execute(self,strcmd):
        objsrv = self.objserver
        objsrv.exists(strcmd)

    def upload(self, pathlocal,pathdirserv,fr=1):
        if self.objserver is None:
            host = self.dicaccess["host"]
            print(f"Sftp: file {pathlocal} not uploaded! not connected to server {host}")
            return 0
        # print(pathlocal); sys.exit()
        if not os.path.exists(pathlocal):
            print(f"Sftp: file {pathlocal} not uploaded! file does not exist")
            return 0

        objsrv = self.objserver
        filename = os.path.basename(pathlocal)
        fileserver = pathdirserv +"/"+filename

        if objsrv.isfile(fileserver):
            if fr==1:
                self.execute(f"rm -f {fileserver}")
            else:
                print(f"Sftp: file {pathlocal} not uploaded! file {fileserver}  already exists in server")
                return 0
        
        if not objsrv.isdir(pathdirserv):
            # print(objsrv.listdir())
            # print(objsrv.pwd) devuelve / que es equivalente a $HOME pero no puedo ni debo usar $HOME o ~
            print(f"Sftp: file {pathlocal} not uploaded! dir {pathdirserv}  does not exist in server")
            return 0

        objsrv.chdir(pathdirserv)
        objsrv.put(pathlocal)
        
    
    def close(self):
        if self.objserver is not None:
            self.objserver.close
            self.objserver = None

    def is_connected(self):
        return self.objserver is not None




