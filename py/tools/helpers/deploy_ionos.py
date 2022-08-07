import os
import time
from tools.tools import *
from tools.sftpit import Sftpit
from tools.sshit import Sshit
from tools.zipit import zipdir, zipfilesingle


class BEDEPLOYTYPE:
    NO_VENDOR = "no-vendor"
    NO_DB = "no-db"
    NO_CODE = "no-code"


class DEPLOYSTEP:
    GENERAL = "general"
    DB = "db"
    SOURCEBE = "sourcebe"
    SOURCEFRONT = "sourcefront"
    PICTURES = "pictures"


class DEPLOYMOMENT:
    PRE = "pre"
    POST = "post"


class DeployIonos:

    def __init__(self, dicproject):
        self.dicproject = dicproject

    def _get_sshaccess_back(self):
        return self.dicproject[DEPLOYSTEP.SOURCEBE]["remote"]

    def _get_sshaccess_front(self):
        return self.dicproject[DEPLOYSTEP.SOURCEFRONT]["remote"]

    def _get_sshaccess_pictures(self):
        return self.dicproject["pictures"]["remote"]

    # no va!!
    def _rm_oldzip(self, pathupload):
        dicaccess = self._get_sshaccess_front()
        ssh = Sshit(dicaccess)
        ssh.connect()
        ssh.cmd(f"cd $HOME/{pathupload}")
        #  esto da error, se ejecuta despues de la subida, se queda el contexto abierto y se ejecuta al final
        # en el otro excecute
        #  ssh.cmd("rm -fr build.zip")
        ssh.execute()
        ssh.close()
        time.sleep(5)
        # print("end remove zip")

    # ====================================================================
    # db
    # ====================================================================
    def _get_maxdbfile(self):
        belocal = self.dicproject[DEPLOYSTEP.SOURCEBE]["local"]
        pathdb = f"{belocal}/db"
        files = scandir(pathdb)
        files.sort(reverse=True)  # order by desc
        # pr(files);pr(pathdb); die("pathdb")
        files = filter(lambda filename: filename.endswith(".sql"), files)
        files = list(files)
        if not files:
            return

        return files[0]
        # return f"{pathdb}/{files[0]}"

    def dbrestore(self):
        # necesito la copia en prod, cuidadin pq se sube todo el código
        # self.gitpull()
        lastdbdump = self._get_maxdbfile()
        if not lastdbdump:
            print(f"dbrestore: no dump .sql file found!")
            return

        localdbname = self.dicproject["db"]["dblocal"]
        pathremote = self.dicproject[DEPLOYSTEP.SOURCEBE]["remote"]["path"]
        # remote db
        dbname = self.dicproject["db"]["remote"]["database"]
        dbserver = self.dicproject["db"]["remote"]["server"]
        dbuser = self.dicproject["db"]["remote"]["user"]
        dbpassword = self.dicproject["db"]["remote"]["password"]

        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        ssh.connect()

        pre = self._get_deploy_cmds(DEPLOYSTEP.DB, DEPLOYMOMENT.PRE)
        for cmd in pre:
            ssh.cmd(cmd)

        ssh.cmd(f"cd $HOME/{pathremote}/db")
        ssh.cmd(f"cp {lastdbdump} temp.sql")
        ssh.cmd(f"python $HOME/mi_python/replacer.py {localdbname} {dbname} ./temp.sql")
        ssh.cmd(
            f"mysql --host={dbserver} --user={dbuser} --password=\"{dbpassword}\" {dbname} < $HOME/{pathremote}/db/temp.sql")
        ssh.cmd("rm temp.sql")
        ssh.cmd(f"cd $HOME/{pathremote}")
        ssh.cmd(f"rm -fr var/cache")

        pre = self._get_deploy_cmds(DEPLOYSTEP.DB, DEPLOYMOMENT.POST)
        for cmd in pre:
            ssh.cmd(cmd)

        ssh.execute()
        ssh.close()

    # ====================================================================
    # backend
    # ====================================================================
    @staticmethod
    def _composer_zip(pathfrom, pathto):
        zipdir(pathfrom, pathto)

    def _composer_upload(self, pathfrom, pathto):
        # la conexión no se hace a un directorio con ruta absoluta sino que 
        # se toma la carpeta de destino como absoluta, esto es para evitar que se tenga acceso a carpetas padres
        # por lo tanto para mi "/" seria equivalente a $HOME
        dicaccess = self._get_sshaccess_back()
        sftp = Sftpit(dicaccess)
        sftp.connect()
        if sftp.is_connected():
            sftp.upload(pathfrom, pathto)
            sftp.close()

    def _composer_unzip(self, pathupload):
        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        ssh.connect()
        ssh.cmd(f"cd $HOME/{pathupload}")
        ssh.cmd("rm -fr vendor")
        ssh.cmd("unzip vendor.zip -d ./")
        #  no puedo borrarlo inmediatamente pq puede que la descompresion no haya finalizado
        # ssh.cmd("rm -f vendor.zip")
        ssh.execute()
        ssh.close()

    def composer_vendor(self):
        # /Users/ioedu/projects/prj_tinymarket/backend_web
        belocal = self.dicproject[DEPLOYSTEP.SOURCEBE]["local"]
        pathremote = self.dicproject[DEPLOYSTEP.SOURCEBE]["remote"]["path"]

        pathvendor = f"{belocal}/vendor"
        pathzip = f"{belocal}/vendor.zip"

        self._composer_zip(pathvendor, pathzip)
        # @todo aqui deberia borra e zip que existiera antes del upload
        self._composer_upload(pathzip, pathremote)  # sftp
        self._composer_unzip(pathremote)  # ssh
        os.remove(pathzip)

    def gitpull(self, rmcache=False):
        pathremote = self.dicproject[DEPLOYSTEP.SOURCEBE]["remote"]["path"]

        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        ssh.connect()
        ssh.cmd(f"cd $HOME/{pathremote}")
        ssh.cmd("git pull")
        if rmcache:
            ssh.cmd(f"rm -fr var/cache")
        ssh.execute()
        ssh.close()

    def _deploy_pre(self):
        cmds = self._get_deploy_cmds(DEPLOYSTEP.GENERAL, DEPLOYMOMENT.PRE)
        if not cmds:
            return

        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        ssh.connect()
        for cmd in cmds:
            ssh.cmd(cmd)
        ssh.execute()
        ssh.close()

    def _deploy_post(self):
        cmds = self._get_deploy_cmds(DEPLOYSTEP.GENERAL, DEPLOYMOMENT.POST)
        if not cmds:
            return

        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        ssh.connect()
        for cmd in cmds:
            ssh.cmd(cmd)
        ssh.execute()
        ssh.close()

    def _get_deploy_cmds(self, step=DEPLOYSTEP.GENERAL, moment=DEPLOYMOMENT.PRE):
        if step == DEPLOYSTEP.GENERAL:
            step = self.dicproject.get("deploy", {})
        elif step == DEPLOYSTEP.DB:
            step = self.dicproject.get(DEPLOYSTEP.DB, {}).get("deploy", {})
        elif step == DEPLOYSTEP.SOURCEBE:
            step = self.dicproject.get(DEPLOYSTEP.SOURCEBE, {}).get("deploy", {})
        else:
            step = {}

        if not step:
            return

        cmds = step.get(moment, [])
        cmds = filter(lambda cmd: not cmd.startswith("//"), cmds)
        return cmds

    def _deploy_pro(self):
        pre = self.dicproject.get("deploy", {}).get("pro", [])
        pre = filter(lambda cmd: not cmd.startswith("//"), pre)
        if not pre:
            return

        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        ssh.connect()
        for cmd in pre:
            ssh.cmd(cmd)
        ssh.execute()
        ssh.close()

    def backend(self, deploytype: str = ""):
        self._deploy_pre()

        if not deploytype:
            self.gitpull()
            self.composer_vendor()
            self.dbrestore()

        if deploytype == BEDEPLOYTYPE.NO_VENDOR:
            self.gitpull()
            self.dbrestore()

        if deploytype == BEDEPLOYTYPE.NO_CODE:
            self.composer_vendor()
            self.dbrestore()

        if deploytype == BEDEPLOYTYPE.NO_DB:
            self.gitpull()
            self.composer_vendor()

        self._deploy_post()

    # ====================================================================
    # pictures
    # ====================================================================
    def _pictures_zip(self, pathfrom, pathto):
        zipdir(pathfrom, pathto)

    def _pictures_upload(self, pathfrom, pathto):
        dicaccess = self._get_sshaccess_pictures()
        sftp = Sftpit(dicaccess)
        sftp.connect()
        if sftp.is_connected():
            sftp.upload(pathfrom, pathto)
            sftp.close()

    def _pictures_unzip(self, pathupload):
        dicaccess = self._get_sshaccess_pictures()
        ssh = Sshit(dicaccess)
        ssh.connect()
        pathup = f"$HOME/{pathupload}"
        print(f"upload path: {pathup}")
        ssh.cmd(f"cd {pathup}")
        ssh.cmd("rm -fr build")
        ssh.cmd("unzip pictures.zip -d ./")
        #  no puedo borrarlo inmediatamente pq puede que la descompresion no haya finalizado
        # ssh.cmd("rm -f vendor.zip")
        ssh.execute()
        ssh.close()

    def pictures(self):
        belocal = self.dicproject["pictures"]["local"]
        pathremote = self.dicproject["pictures"]["remote"]["path"]

        pathpictures = f"{belocal}/pictures"
        pathzip = f"{belocal}/pictures.zip"

        self._pictures_zip(pathpictures, pathzip)
        self._pictures_upload(pathzip, pathremote)
        self._pictures_unzip(pathremote)

    # ====================================================================
    # frontend
    # ====================================================================
    def _isvue(self, pathlocal):
        return is_file(pathlocal + "/src/App.vue")

    def _build_zip(self, pathfrom, pathto):
        zipdir(pathfrom, pathto)

    def _npmbuild(self, pathlocal):
        if is_dir(pathlocal + "/build"):
            # react
            sh(f"cd {pathlocal}; sh -ac '. .env.build; node ./scripts/build-non-split.js;'; rm build.zip")
        elif self._isvue(pathlocal):
            # vue
            sh(f"cd {pathlocal}; npm run build; rm build.zip")

    def _build_upload(self, pathfrom, pathto):
        dicaccess = self._get_sshaccess_front()
        sftp = Sftpit(dicaccess)
        sftp.connect()
        if sftp.is_connected():
            sftp.upload(pathfrom, pathto)
            sftp.close()

    def _build_unzip(self, pathupload, name="build"):
        dicaccess = self._get_sshaccess_front()
        ssh = Sshit(dicaccess)
        ssh.connect()
        pathup = f"$HOME/{pathupload}"
        print(f"upload path: {pathup}")
        ssh.cmd(f"cd {pathup}")
        ssh.cmd(f"rm -fr {name}")
        ssh.cmd(f"unzip {name}.zip -d ./")
        # en caso de vue se descomprime como dist
        ssh.cmd(f"mv dist {name}")
        #  no puedo borrarlo inmediatamente pq puede que la descompresion no haya finalizado
        # ssh.cmd("rm -f vendor.zip")
        ssh.execute()
        ssh.close()

    def _build_rename(self, pathupload):
        dicaccess = self._get_sshaccess_front()
        ssh = Sshit(dicaccess)
        ssh.connect()
        pathup = f"$HOME/{pathupload}"
        print(f"upload path: {pathup}")
        ssh.cmd(f"cd {pathup}")
        # elimino todo lo anterior
        ssh.cmd("rm -fr ./react")
        ssh.cmd(f"mv ./build ./react")
        ssh.cmd("rm -f build.zip")
        ssh.execute()
        ssh.close()

    def frontend(self):
        belocal = self.dicproject[DEPLOYSTEP.SOURCEFRONT]["local"]
        pathremote = self.dicproject[DEPLOYSTEP.SOURCEFRONT]["remote"]["path"]
        if not pathremote or not belocal:
            return

        pathbuild = f"{belocal}/build"
        pathzip = f"{belocal}/build.zip"

        # el caso de vue
        if self._isvue(belocal):
            pathbuild = f"{belocal}/dist"
            pathzip = f"{belocal}/build.zip"

        #  este no me vale, me elimina el zip juste despues de haberlo subido
        #  self._rm_oldzip(pathremote)

        # return
        self._npmbuild(belocal)
        self._build_zip(pathbuild, pathzip)
        self._build_upload(pathzip, pathremote)
        self._build_unzip(pathremote)

    def _build_remove(self, arfiles):
        belocal = self.dicproject["frontendembed"]["local"]
        pathbuild = f"{belocal}/build"
        for file in arfiles:
            sh(f"rm -f {pathbuild}/{file}")

    def frontendembed(self):
        belocal = self.dicproject["frontendembed"]["local"]
        pathremote = self.dicproject["frontendembed"]["remote"]["path"]
        if not belocal or not pathremote:
            return

        pathbuild = f"{belocal}/build"
        pathzip = f"{belocal}/build.zip"

        #  este no me vale, me elimina el zip juste despues de haberlo subido
        #  self._rm_oldzip(pathremote)

        # return
        sh(f"rm -f {pathzip}")
        self._npmbuild(belocal)
        self._build_remove(["index.html", ".htaccess"])
        self._build_zip(pathbuild, pathzip)
        self._build_upload(pathzip, pathremote)
        self._build_unzip(pathremote)
        self._build_rename(pathremote)
