import pysftp
import sys
import os

# https://stackoverflow.com/questions/432385/sftp-in-python-platform-independent
class Sftp:
    objserver = None

    def __init__(self, dicaccess):
        print("Sftp initialized...")
        self.dicaccess = dicaccess

    def connect(self):
        config = self.dicaccess
        host = config["host"]
        user = config["user"]
        password = config["password"]
        path = config["path"]
        port = config["port"] if "port" in config.keys() else 22 # entero

        #self.objserver = pysftp.Connection(host=host, username=user, password=password, port=port)
        
        print(f"connected to:"+str(self.objserver)+f" host: {host}")

    def execute(self,strcmd):
        objsrv = self.objserver
        objsrv.exists(strcmd)


    def upload(self, pathlocal,pathdirserv,fr=1):
        # print(pathlocal); sys.exit()
        if not os.path.exists(pathlocal):
            print(f"sftp: file {pathlocal} not uploaded! file does not exist")
            return 0

        objsrv = self.objserver
        filename = os.path.basename(pathlocal)
        fileserver = pathdirserv +"/"+filename

        if objsrv.isfile(fileserver):
            if fr==1:
                self.execute(f"rm -f {fileserver}")
            else:
                print(f"sftp: file {pathlocal} not uploaded! file {fileserver}  already exists in server")
                return 0
        
        if not objsrv.isdir(pathdirserv):
            # print(objsrv.listdir())
            # print(objsrv.pwd) devuelve / que es equivalente a $HOME pero no puedo ni debo usar $HOME o ~
            print(f"sftp: file {pathlocal} not uploaded! dir {pathdirserv}  does not exist in server")
            return 0

        objsrv.chdir(pathdirserv)
        objsrv.put(pathlocal)
        
    
    def close(self):
        if self.objserver is not None:
            self.objserver.close
            self.objserver = None

    def is_connected(self):
        return self.objserver is not None




