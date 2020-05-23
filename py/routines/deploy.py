"""
hace el deploy de un proyecto en local en prod
ejemplo:
    <prject-id> esta en el config/json
    py.sh <project-id> index deploy
    py.sh tinymarket index deploy
"""

from tools.tools import *
from tools.helpers.deploy_ionos import DeployIonos
from tools.sftpit import Sftp

def index(project):
    pr(f"starting deploy of {project}")
    thisdir = get_dir(__file__)
    pathconfig = get_realpath(thisdir+"/../config/projects.local.json")
    jsonhlp = Json(pathconfig)
    jsonhlp.load_data()
    dicproject = jsonhlp.get_dictbykey("id",project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0
    pr(f"...deploy of {project} has finished")

if __name__ == "__main__":
    index("tinymarket")