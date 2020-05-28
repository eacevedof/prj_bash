"""
module: deploy
- hace el deploy de un proyecto en local en prod
    
ejemplo:
    <prject-id> esta en el config/json
    py.sh <project-id> index deploy
    py.sh deploy tinymarket
    py.sh deploy.composer tinymarket
    py.sh deploy.dbrestore tinymarket
"""
from tools.helpers.deploy_ionos import DeployIonos
from tools.tools import *

def composer(project):
    timeini = get_now()
    pr(f"deply.composer: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    ionos.composer()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")


def dbrestore(project):
    timeini = get_now()
    pr(f"deply.dbrestore: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    ionos.dbrestore()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")


def frontbuild(project):
    timeini = get_now()
    pr(f"frontbuild.dbrestore: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    ionos.frontend()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")


def full(project):
    timeini = get_now()
    pr(f"starting deploy of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    # ppr(dicproject,"DICPROJECT RECUPERADO")
    ionos = DeployIonos(dicproject)
    ionos.backend()
    ionos.frontend()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")

if __name__ == "__main__":
    index("tinymarket")