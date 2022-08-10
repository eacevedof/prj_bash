from tools.sshit import Sshit
import re
import os


class DeployDb:

    def __init__(self, dicproject):
        self.__dicproject = dicproject
        self.__dbnode = self.__dicproject.get("db", {})
