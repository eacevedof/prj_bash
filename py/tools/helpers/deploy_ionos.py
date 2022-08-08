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


class DEPLOYOPTIONS:
    VENDOR_BY_COPY = "vendor-by-copy"
    DB_BY_MIGRATIONS = "db-by-migration"


class DeployIonos:

    def __init__(self, dicproject):
        self.dicproject = dicproject

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
    # db
    # ====================================================================
    @staticmethod
    def __get_files_by_creation_date_desc(dirpath):
        files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
        if not files:
            return []

        files.sort(key=lambda f: os.path.getmtime(os.path.join(dirpath, f)))

        def only_names(path):
            head, tail = os.path.split(path)
            return tail

        return list(map(only_names, files))

    def __get_latest_sqldump_name(self):
        pathdumps = self.dicproject.get(DEPLOYSTEP.DB, {}).get("pathdumps", "")
        files = self.__get_files_by_creation_date_desc(pathdumps)

        filedump = self.dicproject.get(DEPLOYSTEP.DB, {}).get("filename", "")
        files = filter(lambda filename: filename.endswith(".sql"), files)
        if filedump:
            files = filter(lambda filename: filename.find(filedump) != -1, files)
            return files[0] if files else ""

        files = list(files)
        return files[0] if files else ""

    def __restore_from_dump(self):
        options = self.dicproject.get(DEPLOYSTEP.DB, {}).get("deploy", {}).get("options", [])
        if DEPLOYOPTIONS.DB_BY_MIGRATIONS in options:
            return

        lastdbdump = self.__get_latest_sqldump_name()
        if not lastdbdump:
            print(f"sql dump file not found!")
            return

        localdbname = self.dicproject.get(DEPLOYSTEP.DB, {}).get("dblocal", "")
        pathremote = self.dicproject.get(DEPLOYSTEP.DB, {}).get("remote", {}).get("pathdumps", "")
        # remote db
        dbname = self.dicproject.get(DEPLOYSTEP.DB).get("remote", {}).get("database", "")
        dbserver = self.dicproject.get(DEPLOYSTEP.DB).get("remote", {}).get("server", "")
        dbuser = self.dicproject.get(DEPLOYSTEP.DB).get("remote", {}).get("user", "")
        dbpassword = self.dicproject.get(DEPLOYSTEP.DB).get("remote", {}).get("password", "")

        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        ssh.connect()
        ssh.cmd(f"cd {pathremote}")
        ssh.cmd(f"cp {lastdbdump} temp.sql")
        ssh.cmd(f"sed -i 's/ {localdbname}/{dbname}/' ./temp.sql")
        ssh.cmd(
            f"mysql --host={dbserver} --user={dbuser} --password=\"{dbpassword}\" {dbname} < {pathremote}/temp.sql"
        )
        ssh.cmd("rm temp.sql")
        ssh.execute()
        ssh.close()

    def dbrestore(self):
        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        cmds = self.__get_deploy_cmds(DEPLOYSTEP.DB, DEPLOYMOMENT.PRE)
        self.__run_groups_of_cmds(ssh, cmds)

        self.__restore_from_dump()

        cmds = self.__get_deploy_cmds(DEPLOYSTEP.DB, DEPLOYMOMENT.POST)
        self.__run_groups_of_cmds(ssh, cmds)

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
        options = self.dicproject.get(DEPLOYSTEP.SOURCEBE, {}).get("deploy", {}).get("options", [])
        if DEPLOYOPTIONS.VENDOR_BY_COPY not in options:
            return

        belocal = self.dicproject.get(DEPLOYSTEP.SOURCEBE, {}).get("local", "")
        pathremote = self.dicproject.get(DEPLOYSTEP.SOURCEBE, {}).get("remote", {}).get("path", "")
        if not belocal or not pathremote:
            return

        pathvendor = f"{belocal}/vendor"
        pathzip = f"{belocal}/vendor.zip"

        self._composer_zip(pathvendor, pathzip)
        # @todo aqui deberia borra e zip que existiera antes del upload
        self._composer_upload(pathzip, pathremote)  # sftp
        self._composer_unzip(pathremote)  # ssh
        os.remove(pathzip)

    def __get_deploy_cmds(self, deploy=DEPLOYSTEP.GENERAL, moment=DEPLOYMOMENT.PRE):
        if deploy == DEPLOYSTEP.GENERAL:
            deploydata = self.dicproject.get("deploy", {})
        elif deploy == DEPLOYSTEP.DB:
            deploydata = self.dicproject.get(DEPLOYSTEP.DB, {}).get("deploy", {})
        elif deploy == DEPLOYSTEP.SOURCEBE:
            deploydata = self.dicproject.get(DEPLOYSTEP.SOURCEBE, {}).get("deploy", {})
        else:
            return []

        allcmds = deploydata.get(moment, [])
        mapped = []
        for cmds in allcmds:
            if not cmds:
                continue
            cmds = filter(lambda cmd: not cmd.startswith("//"), cmds)
            if cmds:
                mapped.append(list(cmds))
        return mapped

    @staticmethod
    def __run_groups_of_cmds(ssh, allcmds):
        if not allcmds:
            return

        for cmds in allcmds:
            ssh.connect()
            for cmd in cmds:
                ssh.cmd(cmd)
            ssh.execute()
            ssh.close()
            ssh.clear()

    def git_pull_be(self):
        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        cmds = self.__get_deploy_cmds(DEPLOYSTEP.SOURCEBE, DEPLOYMOMENT.PRE)
        self.__run_groups_of_cmds(ssh, cmds)

        cmds = self.__get_deploy_cmds(DEPLOYSTEP.SOURCEBE, DEPLOYMOMENT.POST)
        self.__run_groups_of_cmds(ssh, cmds)

    def deploy_pre_general(self):
        cmds = self.__get_deploy_cmds(DEPLOYSTEP.GENERAL, DEPLOYMOMENT.PRE)
        if not cmds:
            return

        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        ssh.connect()
        self.__run_groups_of_cmds(ssh, cmds)

    def deploy_post_general(self):
        cmds = self.__get_deploy_cmds(DEPLOYSTEP.GENERAL, DEPLOYMOMENT.POST)
        if not cmds:
            return

        dicaccess = self._get_sshaccess_back()
        ssh = Sshit(dicaccess)
        self.__run_groups_of_cmds(ssh, cmds)

    def backend(self, deploytype: str = ""):
        self.deploy_pre_general()

        if not deploytype:
            self.git_pull_be()
            self.composer_vendor()
            self.dbrestore()

        if deploytype == BEDEPLOYTYPE.NO_VENDOR:
            self.git_pull_be()
            self.dbrestore()

        if deploytype == BEDEPLOYTYPE.NO_CODE:
            self.composer_vendor()
            self.dbrestore()

        if deploytype == BEDEPLOYTYPE.NO_DB:
            self.git_pull_be()
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
