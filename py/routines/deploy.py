"""
module: deploy
- hace el deploy de un proyecto en local en prod
    
ejemplo:
    <prject-id> esta en el config/json
    py.sh <project-id> index deploy
    py.sh deploy tinymarket  #full deploy front and back
    py.sh deploy.composer tinymarket
    py.sh deploy.dbrestore tinymarket
"""
from tools.helpers.deploy_ionos import DeployIonos
from tools.tools import *

# py.sh deploy.composer tinymarket
def composer(project):
    timeini = get_now()
    pr(f"deploy.composer: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    ionos.composer()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")

# py.sh deploy.dbrestore tinymarket
def dbrestore(project):
    timeini = get_now()
    pr(f"deploy.dbrestore: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    ionos.dbrestore()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")

# py.sh deploy.pictures tinymarket
def pictures(project):
    timeini = get_now()
    pr(f"deploy.pictures: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    ionos.pictures()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")

# py.sh deploy.frontbuild tinymarket
def frontbuild(project):
    timeini = get_now()
    pr(f"deploy.frontbuild: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    ionos.frontend()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")


# py.sh deploy tinymarket
def index(project):
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
    ionos.pictures()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")
