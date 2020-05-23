import pysftp
import sys
import os

# https://stackoverflow.com/questions/432385/sftp-in-python-platform-independent
class Sftp:
    trigger = ""
    objserver = None

    def __init__(self, dicproject,trigger):
        print("Sftp...")
        self.dicproject = dicproject
        self.trigger = trigger # backend, frontend, db
        pass

    def _backend(self):
        pass

    def connect(self):
        dicprod = self.dicproject[self.trigger]["prod"]
        host = dicprod["host"]
        user = dicprod["user"]
        password = dicprod["password"]
        path = dicprod["path"]

#home337670657.1and1-data.host
        # self.objserver = pysftp.Connection(host=host, username=user, password=password)
        
        print(f"connected to:"+str(self.objserver)+f" host: {host}")

    def execute(self,strcmd):
        objsrv = self.objserver
        objsrv.exists(strcmd)


    def upload(pathlocal,pathdirserv,fr=1):
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




