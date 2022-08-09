from deploy_types import DEPLOYSTEP
from tools.sshit import Sshit


class DeployDb:

    def __init__(self, dicproject):
        self.__dicproject = dicproject
        self.__dbnode = self.dicproject.get(DEPLOYSTEP.DB, {})
        self.__ssh = self.__load_ssh()
        self.__load_replace_tags()

    def __load_ssh(self):
        credentials = self.__dbnode.get("remote", {}).get("ssh", {})
        return Sshit(credentials)

    def __load_replace_tags(self):
        origin = self.__dbnode.get("origin", {})
        remote = self.__dbnode.get("remote", {})
        self.__replace_tags = {
            "db.origin.pathdumps": origin.get("pathdumps",""),
            "db.origin.filepattern": origin.get("filepattern",""),
            "db.origin.server": origin.get("server",""),
            "db.origin.port": origin.get("port",""),
            "db.origin.database": origin.get("database",""),
            "db.origin.user": origin.get("user",""),
            "db.origin.password": origin.get("password",""),

            "remote.pathdumps": remote.get("pathdumps",""),
            "remote.server": remote.get("server",""),
            "remote.port": remote.get("port",""),
            "remote.database": remote.get("database",""),
            "remote.user": remote.get("user",""),
            "remote.password": remote.get("password",""),
        }



    def get_replace_tags(self):
        return self.__replace_tags

    def __get_deploy_cmds(self):
        allcmds = self.__dbnode.get("deploy",{}).get("steps",[])
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
        keys = self.__replace_tags.keys()
        for key in keys:
            cmd = cmd.replace(f"%{key}%", self.__replace_tags.get(key, ""))
        return cmd

    def __run_groups_of_cmds(self, allcmds):
        if not allcmds:
            return

        for group in allcmds:
            self.__ssh.connect()
            for cmd in group:
                cmd = self.__get_replaced(cmd)
                self.__ssh.cmd(cmd)
            self.__dbnode.execute()
            self.__ssh.close()
            self.__ssh.clear()

    def deplopy(self):
        allcmds = self.__get_deploy_cmds()
        if not allcmds:
            return

        self.__run_groups_of_cmds(allcmds)

