from .deploy_base import DeployBase
from tools.sftpit import Sftpit
from tools.zipit import zipdir, zipfilesingle


class DeployPictures(DeployBase):

    def __init__(self, dicproject):
        # to-do all
        DeployBase.__init__(self, dicproject)
        self._node = self._dicproject.get("frontend", {})
        self._ssh = self._load_ssh()
        self._replace_tags = self.__load_replace_tags()

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
