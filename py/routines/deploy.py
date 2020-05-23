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
    pathjson = thisdir+"/../config/projects.local.json"
    pathconfig = get_realpath(pathjson)
    #pr(pathconfig);die()
    jsonhlp = Json(pathconfig)
    jsonhlp.load_data()
    dicproject = jsonhlp.get_dictbykey("id",project)
    pr(dicproject)
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    # la conexión no se hace a un directorio con ruta absoluta sino que 
    # se toma la carpeta de destino como absoluta, esto es para evitar que se tenga acceso a carpetas padres
    # por lo tanto para mi "/" seria equivalente a $HOME
    sftp = Sftp(dicproject,"backend")
    sftp.connect()
    if sftp.is_connected():
        sftp.upload(pathconfig, "/mi_temporal")
        sftp.close()

    pr(f"...deploy of {project} has finished")

if __name__ == "__main__":
    index("tinymarket")