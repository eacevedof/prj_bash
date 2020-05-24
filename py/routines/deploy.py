"""
hace el deploy de un proyecto en local en prod
ejemplo:
    <prject-id> esta en el config/json
    py.sh <project-id> index deploy
    py.sh tinymarket index deploy
"""
from tools.helpers.deploy_ionos import DeployIonos
from tools.tools import *

def index(project):
    timeini = get_now()
    pr(f"starting deploy of {project}. {timeini}")
    pathconfig = get_path_config_json()
    jsonhlp = Json(pathconfig)
    jsonhlp.load_data()
    dicproject = jsonhlp.get_dictbykey("id",project)
    # ppr(dicproject["backend"]["prod"]); # die()
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    #ionos.gitpull()
    #ionos.composer()
    ionos.db()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")

if __name__ == "__main__":
    index("tinymarket")