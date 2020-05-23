from tools.tools import *
from tools.helpers.deploy_ionos import DeployIonos
from tools.sftpit import Sftp

def index(project):
    json = Json()
    json.load_data()
    dicproject = json.get_dictbykey("id",project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0


    