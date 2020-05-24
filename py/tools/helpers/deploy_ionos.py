import os
from tools.tools import *
from tools.sftpit import Sftpit
from tools.sshit import Sshit
from tools.zipit import zipdir, zipfilesingle

class DeployIonos:

    def __init__(self, dicproject):
        self.dicproject = dicproject
        pass

    def _get_sshaccess(self):
        return self.dicproject["backend"]["prod"]

    def gitpull(self):
        pathremote = self.dicproject["backend"]["prod"]["path"]
        
        dicaccess = self._get_sshaccess()
        ssh = Sshit(dicaccess)
        ssh.connect()
        ssh.cmd(f"cd $HOME/{pathremote}")
        ssh.cmd("git pull")
        ssh.execute()
        ssh.close()

    def _composer_zip(self, pathfrom, pathto):
        zipdir(pathfrom, pathto)

    def _composer_upload(self,pathfrom,pathto):
        # la conexión no se hace a un directorio con ruta absoluta sino que 
        # se toma la carpeta de destino como absoluta, esto es para evitar que se tenga acceso a carpetas padres
        # por lo tanto para mi "/" seria equivalente a $HOME
        dicaccess = self._get_sshaccess()
        sftp = Sftpit(dicaccess)
        sftp.connect()
        if sftp.is_connected():
            sftp.upload(pathfrom, pathto)
            sftp.close()

    def _composer_unzip(self,pathupload):
        dicaccess = self._get_sshaccess()
        ssh = Sshit(dicaccess)
        ssh.connect()
        ssh.cmd(f"cd $HOME/{pathremote}")
        ssh.cmd("rm -fr vendor")
        ssh.cmd("unzip vendor.zip -d ./")
        ssh.cmd("rm -f vendor.zip")
        ssh.execute()
        ssh.close()

    def composer(self):
        # /Users/ioedu/projects/prj_tinymarket/backend_web
        belocal = self.dicproject["backend"]["local"]
        pathremote = self.dicproject["backend"]["prod"]["path"]

        pathvendor = f"{belocal}/vendor"
        pathzip = f"{belocal}/vendor.zip"

        self._composer_zip(pathvendor,pathzip)
        self._composer_upload(pathzip, pathremote) # sftp
        self._composer_unzip(pathremote) # ssh

    def backend(self):
        pass

    def frontend(self):
        pass

    def _get_maxdbfile(self):
        belocal = self.dicproject["backend"]["local"]
        pathdb = f"{belocal}/db"        
        files = scandir(pathdb).sort(reverse = True)
        return files[0]

    def db(self):
        lastdbdump = self._get_maxdbfile()
        localdbname = self.dicproject["db"]["dblocal"]
        pathremote = self.dicproject["backend"]["prod"]["path"]
        # remote db
        dbname = self.dicproject["db"]["prod"]["database"]
        dbserver = self.dicproject["db"]["prod"]["server"]
        dbuser = self.dicproject["db"]["prod"]["user"]
        dbpassword = self.dicproject["db"]["prod"]["password"]

        dicaccess = self._get_sshaccess()
        ssh = Sshit(dicaccess)
        ssh.connect()        
        ssh.cmd(f"cd $HOME/{pathremote}/db")
        ssh.cmd(f"cp {lastdbdump} temp.sql")
        ssh.cmd(f"python $HOME/mi_python/replacer.py {localdbname} {dbname} ./temp.sql")
        ssh.cmd(f"mysql --host=db5000452636.hosting-data.io --user={dbuser} --password={dbpassword} {dbname} < $HOME/{pathremote}/db/temp.sql")
        ssh.cmd("rm temp.sql")
        ssh.execute()
        ssh.close()
    