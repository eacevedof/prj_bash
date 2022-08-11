from tools.sshit import Sshit
from tools.sftpit import Sftpit
from .deploy_step_exception import DeployStepException
from tools.zipit import zipdir, zipfilesingle
import os


class DeployTag:
    FINISH_ON_ERROR = "%finish_on_error%"
    FN_DEFAULT = "%fn_default%"
    FN_UPLOAD = "%fn_upload%"
    FN_UPLOAD_ZIPPED = "%fn_upload_zipped%"

class DeployBase:
    _dicproject = {}
    _node = {}
    _ssh = None
    _replace_tags = {}

    def __init__(self, dicproject):
        self._dicproject = dicproject
        self._node = {}

    def _load_ssh(self):
        credentials = self._node.get("remote", {}).get("ssh", {})
        return Sshit(credentials)

    def get_replace_tags(self):
        return self._replace_tags

    def _get_step_cmds(self):
        allcmds = self._node.get("deploy", {}).get("steps", [])
        if not allcmds:
            return []

        mapped = []
        for cmds in allcmds:
            if not cmds:
                continue
            cmds = filter(lambda cmd: not cmd.startswith("//"), cmds)
            cmds = filter(lambda cmd: bool(cmd.strip()), cmds)
            cmds = list(cmds)
            if cmds:
                mapped.append(cmds)
        return mapped

    def __get_replaced(self, cmd):
        keys = self._replace_tags.keys()
        for key in keys:
            cmd = cmd.replace(f"%{key}%", self._replace_tags.get(key, ""))
        return cmd

    def __upload(self, pathfrom, pathto):
        credentials = self._node.get("remote", {}).get("ssh", {})
        sftp = Sftpit(credentials)
        sftp.connect()
        if sftp.is_connected():
            ok = sftp.upload(pathfrom, pathto)
            sftp.close()
            if not ok:
                raise DeployStepException(f"upload error (nok) from:{pathfrom} to {pathto}")
            return
        raise DeployStepException(f"upload error from:{pathfrom} to {pathto}")

    def __upload_zipped(self, pathfrom, pathto):
        credentials = self._node.get("remote", {}).get("ssh", {})
        sftp = Sftpit(credentials)
        sftp.connect()
        if sftp.is_connected():
            folderzip = os.path.basename(pathfrom)+".zip"
            pathzip = f"{pathfrom}/../{folderzip}"
            zipdir(pathfrom, f"{pathfrom}/../{folderzip}")
            ok = sftp.upload(pathzip, f"{pathto}/{folderzip}")
            sftp.close()
            if not ok:
                raise DeployStepException(f"upload error (nok) from:{pathfrom} to {pathto}")
            return
        raise DeployStepException(f"upload error from:{pathfrom} to {pathto}")

    def __cmd_upload(self, cmd):
        parts = cmd.split(" ")
        del parts[0]
        if len(parts) == 2:
            pathfrom = str(parts[0]).strip()
            pathto = str(parts[1]).strip()
            self.__upload(pathfrom, pathto)

    def __cmd_upload_zipped(self, cmd):
        parts = cmd.split(" ")
        del parts[0]
        if len(parts) == 2:
            pathfrom = str(parts[0]).strip()
            pathto = str(parts[1]).strip()
            self.__upload_zipped(pathfrom, pathto)

    def _run_groups_of_cmds(self, allcmds):
        for group in allcmds:
            self._ssh.connect()
            self._ssh.clear()
            handle_error = True if DeployTag.FINISH_ON_ERROR in group else False
            for cmd in group:
                if DeployTag.FINISH_ON_ERROR in cmd:
                    continue
                cmd = self.__get_replaced(cmd)
                if DeployTag.FN_UPLOAD in cmd:
                    self.__cmd_upload(cmd)
                    continue
                if DeployTag.FN_UPLOAD_ZIPPED in cmd:
                    self.__cmd_upload_zipped(cmd)
                    continue
                self._ssh.cmd(cmd)
            self._ssh.execute()
            self._ssh.close()
            if handle_error and (self._ssh.error or "ERRORS!" in self._ssh.success):
                raise DeployStepException(self._ssh.error)
