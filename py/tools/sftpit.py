import pysftp
import sys
import os
import copy


# https://stackoverflow.com/questions/432385/sftp-in-python-platform-independent
class Sftpit:
    objserver = None

    def __init__(self, dicaccess):
        print("Sftpit: initializing...")
        self.dicaccess = dicaccess.copy()

        if "hostname" in self.dicaccess:
            self.dicaccess["host"] = self.dicaccess.get("hostname")
            self.dicaccess.pop("hostname")

        if "key_filename" in self.dicaccess:
            self.dicaccess["private_key"] = self.dicaccess.get("key_filename")
            self.dicaccess.pop("key_filename")

    def connect(self):
        print("Sftpit: trying to connect...")
        config = copy.deepcopy(self.dicaccess)
        host = config["host"]
        if "path" in config.keys():
            del config["path"]
        # print(config);sys.exit()
        try:
            # self.objserver = pysftp.Connection(host=host, username=user, password=password, port=port)
            self.objserver = pysftp.Connection(**config)
            print(f"Sftpit: connected to host: {host}")
        except Exception as error:
            self.objserver = None
            print(f"Sftpit: error trying to connect to {host} error: {error}")

    def execute(self, strcmd):
        print(f"Sftpit: executing: {strcmd}")
        objsrv = self.objserver
        objsrv.execute(strcmd)

    def upload(self, pathlocal, pathdirserv, fr=1):
        filesize = os.path.getsize(pathlocal)
        print(f"Sftpit: trying to upload {pathlocal} ({filesize})...")
        if self.objserver is None:
            host = self.dicaccess["host"]
            print(f"Sftpit: file {pathlocal} not uploaded! not connected to server {host}")
            return 0
        # print(pathlocal); sys.exit()
        if not os.path.exists(pathlocal):
            print(f"Sftpit: file {pathlocal} not uploaded! file does not exist")
            return 0

        objsrv = self.objserver
        filename = os.path.basename(pathlocal)
        fileserver = pathdirserv + "/" + filename

        if objsrv.isfile(fileserver):
            if fr == 1:
                self.execute(f"rm -f {fileserver}")
            else:
                print(f"Sftpit: file {pathlocal} not uploaded! file {fileserver}  already exists in server")
                return 0

        if not objsrv.isdir(pathdirserv):
            # print(objsrv.listdir())
            # print(objsrv.pwd) devuelve / que es equivalente a $HOME pero no puedo ni debo usar $HOME o ~
            print(f"Sftpit: file {pathlocal} not uploaded! dir {pathdirserv}  does not exist in server")
            return 0

        objsrv.chdir(pathdirserv)
        objsrv.put(pathlocal)
        print(f"Sftpit: upload of {pathlocal} finished")
        return 1

    def download(self, pathfrom, pathto):
        print(f"Sftpit: downloading from:{pathfrom} to:{pathto}")
        objsrv = self.objserver
        objsrv.get(pathfrom, pathto)

    def close(self):
        if self.objserver is not None:
            self.objserver.close
            self.objserver = None

    def is_connected(self):
        return self.objserver is not None
