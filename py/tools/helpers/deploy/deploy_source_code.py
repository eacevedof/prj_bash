from .deploy_base import DeployBase

from tools.sftpit import Sftpit
from tools.zipit import zipdir, zipfilesingle

from .deploy_step_exception import DeployStepException
import re
import os


class DeploySourceCode(DeployBase):

    def __init__(self, dicproject):
        DeployBase.__init__(self, dicproject)
        self._node = self._dicproject.get("sourcecode", {})
        self._ssh = self._load_ssh()
        self._replace_tags = self.__load_replace_tags()

    def __load_replace_tags(self):
        repo = self._node.get("repository", {})
        origin = self._node.get("origin", {})
        remote = self._node.get("remote", {})
        return {
            "sourcecode.repository.url": repo.get("url",""),
            "sourcecode.repository.branch": repo.get("branch","main"),
            "sourcecode.origin.path": origin.get("path", ""),
            "sourcecode.remote.path": remote.get("path", ""),
            "sourcecode.remote.path_nohome": remote.get("path_nohome", ""),
        }



    def __get_files_by_creation_date_desc(self, filepattern):
        dirpath = self._node.get("origin", {}).get("path", "")
        files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
        files = list(filter(lambda f: ".sql" in f, files))
        if not files:
            return []

        files.sort(key=lambda f: os.path.getmtime(os.path.join(dirpath, f)))

        if filepattern:
            files = list(filter(lambda f: len(re.findall(f"{filepattern}", f, flags=re.IGNORECASE)) > 0, files))

        return files

    @staticmethod
    def __default_cmds():
        return []

    @staticmethod
    def __composer_zip(pathfrom, pathto):
        zipdir(pathfrom, pathto)

    def __composer_upload(self,sftp, pathfrom, pathto):
        sftp.connect()
        if sftp.is_connected():
            sftp.upload(pathfrom, pathto)
            sftp.close()

    def __composer_unzip(self, pathupload):
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

    def _copy_vendor(self):
        # /Users/ioedu/projects/prj_tinymarket/backend_web


        pathvendor = f"{belocal}/vendor"
        pathzip = f"{belocal}/vendor.zip"

        self._composer_zip(pathvendor, pathzip)
        # @todo aqui deberia borra e zip que existiera antes del upload
        self._composer_upload(pathzip, pathremote)  # sftp
        self._composer_unzip(pathremote)  # ssh
        os.remove(pathzip)


    def deploy(self):
        allcmds = self._get_step_cmds()

        def append_default_cms(arcmds):
            if " %fn_default_cmds%" in arcmds:
                return self.__default_cmds()
            return arcmds

        allcmds = list(map(append_default_cms, allcmds))

        self._run_groups_of_cmds(allcmds)

