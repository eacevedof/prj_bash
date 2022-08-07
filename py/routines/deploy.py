"""
module: deploy
- hace el deploy de un proyecto en local en prod
    
ejemplo:
    <prject-id> esta en el config/json
    py.sh <project-id> index deploy
    py.sh deploy tinymarket  #full deploy front and back
    py.sh deploy.composer tinymarket
    py.sh deploy.dbrestore tinymarket
    py.hs deploy.codeonly tinymarket
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
    ionos.composer_vendor()
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
    ionos.git_pull_be() # necesito la copia en prod
    ionos.deploy_pre()
    ionos.dbrestore()
    ionos.deploy_post()
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
    ionos.deploy_pre()
    ionos.pictures()
    ionos.deploy_post()
    timeend = get_now()
    pr(f"...deploy pictures of {project} has finished. ini:{timeini} - end:{timeend}")


# py.sh deploy.frontbuild tinymarket
def frontbuild(project):
    timeini = get_now()
    pr(f"deploy.frontbuild: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    ionos = DeployIonos(dicproject)
    ionos.deploy_pre()
    ionos.frontend()
    ionos.deploy_post()
    timeend = get_now()
    pr(f"...deploy frontbuild of {project} has finished. ini:{timeini} - end:{timeend}")


# py.sh deploy.frontbuildembed tinymarket
def frontbuildembed(project):
    timeini = get_now()
    pr(f"deploy.frontbuildembed: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    
    ionos = DeployIonos(dicproject)
    ionos.deploy_pre()
    ionos.frontendembed()
    ionos.deploy_post()
    timeend = get_now()
    pr(f"...deploy frontbuildembed of {project} has finished. ini:{timeini} - end:{timeend}")


def backend(project, options=""):
    timeini = get_now()
    pr(f"deploy.backend: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0
    
    ionos = DeployIonos(dicproject)
    ionos.backend(options)
    timeend = get_now()
    pr(f"...deploy backend of {project} has finished. ini:{timeini} - end:{timeend}")


def codeonly(project):    
    timeini = get_now()
    pr(f"deploy.codeonly: of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed codeonly: project {project} not found")
        return 0
    
    ionos = DeployIonos(dicproject)
    ionos.deploy_pre()
    ionos.git_pull_be()
    ionos.deploy_post()
    timeend = get_now()
    pr(f"...deploy codeonly of {project} has finished. ini:{timeini} - end:{timeend}")


# py.sh deploy tinymarket
def index(project, options=""):
    timeini = get_now()
    pr(f"starting deploy of {project}. {timeini}")

    dicproject = get_dicconfig(project)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    # ppr(dicproject,"DICPROJECT RECUPERADO")
    ionos = DeployIonos(dicproject)
    ionos.backend(options)
    ionos.frontend()
    ionos.pictures()
    timeend = get_now()
    pr(f"...deploy of {project} has finished. ini:{timeini} - end:{timeend}")
