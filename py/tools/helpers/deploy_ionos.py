from tools.tools import *
from tools.sftpit import Sftpit
from tools.sshit import Sshit
from tools.zipit import zipdir, zipfilesingle
from .deploy.deploy_db import DeployDb
from .deploy.deploy_source_code import DeploySourceCode
from .deploy.deploy_step_exception import DeployStepException


class DeployIonos:

    def __init__(self, dicproject):
        self.dicproject = dicproject
        self.__deploydb = DeployDb(dicproject)
        self.__deploysourcecode = DeploySourceCode(dicproject)

    # ====================================================================
    # backend
    # ====================================================================
    def backend(self, deploytype: str = ""):
        try:
            self.__deploydb.deploy()
            self.__deploysourcecode.deploy()

        except DeployStepException as e:
            print(e)

