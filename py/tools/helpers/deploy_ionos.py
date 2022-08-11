import os
import time
from tools.tools import *
from tools.sftpit import Sftpit
from tools.sshit import Sshit
from tools.zipit import zipdir, zipfilesingle
from .deploy.deploy_db import DeployDb
from .deploy.deploy_source_code import DeploySourceCode
from .deploy.deploy_step_exception import DeployStepException

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


class DEPLOYOPTIONS:
    VENDOR_BY_COPY = "vendor-by-copy"
    DB_BY_MIGRATIONS = "db-by-migration"


class DeployIonos:

    def __init__(self, dicproject):
        self.dicproject = dicproject
        self.__deploydb = DeployDb(dicproject)
        self.__deploysourcecode = DeploySourceCode(dicproject)

    def _get_sshaccess_back(self):
        return self.dicproject.get(DEPLOYSTEP.SOURCEBE, {}).get("remote", {})

    def _get_sshaccess_front(self):
        return self.dicproject.get(DEPLOYSTEP.SOURCEFRONT, {}).get("remote", {})

    def _get_sshaccess_pictures(self):
        return self.dicproject.get(DEPLOYSTEP.PICTURES, {}).get("remote", {})

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
    # backend
    # ====================================================================





    def backend(self, deploytype: str = ""):
        try:
            self.__deploydb.deploy()
            self.__deploysourcecode.deploy()

        except DeployStepException as e:
            print(e)

        return
        if not deploytype:
            
            self.composer_vendor()
            self.db_filerestore()

        if deploytype == BEDEPLOYTYPE.NO_VENDOR:
            self.deploy_sourcecode()
            self.db_filerestore()

        if deploytype == BEDEPLOYTYPE.NO_CODE:
            self.composer_vendor()
            self.db_filerestore()

        if deploytype == BEDEPLOYTYPE.NO_DB:
            self.deploy_sourcecode()
            self.composer_vendor()

        self.deploy_post_general()

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
        belocal = self.dicproject.get(DEPLOYSTEP.PICTURES, {}).get("local", "")
        pathremote = self.dicproject.get(DEPLOYSTEP.PICTURES, {}).get("remote", {}).get("path", "")

        if not pathremote or not belocal:
            return

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
        belocal = self.dicproject.get(DEPLOYSTEP.SOURCEFRONT, {}).get("local", "")
        pathremote = self.dicproject.get(DEPLOYSTEP.SOURCEFRONT, {}).get("remote", {}).get("path", "")
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
