from .deploy_base import DeployBase

import re
import os


class DeployDb(DeployBase):

    def __init__(self, dicproject):
        DeployBase.__init__(self, dicproject)
        self._node = self._dicproject.get("db", {})
        self._ssh = self._load_ssh()
        self._replace_tags = self.__load_replace_tags()

    def __load_replace_tags(self):
        origin = self._node.get("origin", {})
        remote = self._node.get("remote", {})
        return {
            "db.origin.pathdumps": origin.get("pathdumps", ""),
            "db.origin.filepattern": origin.get("filepattern", ""),
            "db.origin.server": origin.get("server", ""),
            "db.origin.port": origin.get("port", ""),
            "db.origin.database": origin.get("database", ""),
            "db.origin.user": origin.get("user", ""),
            "db.origin.password": origin.get("password", ""),

            "db.remote.pathdumps": remote.get("pathdumps", ""),
            "db.remote.server": remote.get("server", ""),
            "db.remote.port": remote.get("port", ""),
            "db.remote.database": remote.get("database", ""),
            "db.remote.user": remote.get("user", ""),
            "db.remote.password": remote.get("password", ""),

            "get_last_dump": self.__get_last_dump(),
        }

    def __get_last_dump(self):
        filepattern = self._node.get("origin", {}).get("filepattern", "").strip()
        files = self.__get_files_by_creation_date_desc(filepattern)
        return files[0] if files else ""

    def __get_files_by_creation_date_desc(self, filepattern):
        dirpath = self._node.get("origin", {}).get("pathdumps", "")
        files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
        files = list(filter(lambda f: ".sql" in f, files))
        if not files:
            return []

        files.sort(key=lambda f: os.path.getmtime(os.path.join(dirpath, f)))

        if filepattern:
            files = list(filter(lambda f: len(re.findall(f"{filepattern}", f, flags=re.IGNORECASE)) > 0, files))

        return files

    def deploy(self):
        allcmds = self._get_step_cmds()
        if not allcmds:
            return

        self._run_groups_of_cmds(allcmds)
