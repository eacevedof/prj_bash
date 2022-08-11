from .deploy.deploy_db import DeployDb
from .deploy.deploy_source_code import DeploySourceCode
from .deploy.deploy_step_exception import DeployStepException


class DeployIonos:

    def __init__(self, dicproject):
        self.dicproject = dicproject
        self.__deploydb = DeployDb(dicproject)
        self.__deploysourcecode = DeploySourceCode(dicproject)

    def backend(self):
        try:
            self.__deploydb.deploy()
            self.__deploysourcecode.deploy()
        except DeployStepException as e:
            print(e)

