from .deploy_base import DeployBase
from tools.zipit import zipdir, zipfilesingle

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
            "repository.url": repo.get("url",""),
            "repository.branch": repo.get("branch","main"),
            "sourcecode.origin.path": origin.get("path", ""),
            "sourcecode.remote.path": remote.get("path", ""),
        }

    def __get_last_dump(self):
        filepattern = self._node.get("origin", {}).get("filepattern", "").strip()
        files = self.__get_files_by_creation_date_desc(filepattern)
        return files[0] if files else ""

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
        return [
            "cd %sourcecode.remote.path%",
            "cp %get_last_dump% temp.sql",
            "sed -i 's/%sourcecode.origin.database%/%sourcecode.remote.database%/' ./temp.sql",
            "mysql --host=%sourcecode.remote.server% --user=%sourcecode.remote.user%  --password=\"%sourcecode.remote.password%\" %sourcecode.remote.database% < %sourcecode.remote.path%/temp.sql",
            "rm temp.sql",
        ]

    def deploy(self):
        allcmds = self._get_step_cmds()

        def append_default_cms(arcmds):
            if "%default_cmds%" in arcmds:
                return self.__default_cmds()
            return arcmds

        allcmds = list(map(append_default_cms, allcmds))
        self._run_groups_of_cmds(allcmds)

