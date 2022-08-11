from .deploy_base import DeployBase
from tools.sftpit import Sftpit
from tools.zipit import zipdir, zipfilesingle


class DeployPictures(DeployBase):

    def __init__(self, dicproject):
        # to-do all
        DeployBase.__init__(self, dicproject)
        self._node = self._dicproject.get("pictures", {})
        self._ssh = self._load_ssh()
        self._replace_tags = self.__load_replace_tags()

    # ====================================================================
    # pictures
    # ====================================================================
    def __pictures_zip(self, pathfrom, pathto):
        zipdir(pathfrom, pathto)

    def __pictures_upload(self, pathfrom, pathto):
        dicaccess = self._get_sshaccess_pictures()
        sftp = Sftpit(dicaccess)
        sftp.connect()
        if sftp.is_connected():
            sftp.upload(pathfrom, pathto)
            sftp.close()

    def __pictures_unzip(self, pathupload):
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
        belocal = self._node.get("local", "")
        pathremote = self._node.get("remote", {}).get("path", "")

        if not pathremote or not belocal:
            return

        pathpictures = f"{belocal}/pictures"
        pathzip = f"{belocal}/pictures.zip"

        self.__pictures_zip(pathpictures, pathzip)
        self.__pictures_upload(pathzip, pathremote)
        self.__pictures_unzip(pathremote)
