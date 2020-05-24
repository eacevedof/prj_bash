"""
hace el deploy de un proyecto en local en prod
ejemplo:
    <prject-id> esta en el config/json
    py.sh <project-id> index deploy
    py.sh tinymarket index deploy
"""

from tools.tools import *
from tools.helpers.deploy_ionos import DeployIonos
from tools.sftpit import Sftpit
from tools.sshit import Sshit
from tools.zipit import zipdir, zipfilesingle

def index(project):
    pr(f"starting deploy of {project}")

    pathconfig = get_path_config_json()
    # print(pathconfig)
    pathzip = get_dir(pathconfig)+"/"+get_basename(pathconfig,0)+".zip"
    # print(zipfile); die();
    # zipfilesingle(pathconfig,pathzip)
    pathvendor = "/Users/ioedu/projects/prj_tinymarket-test/backend_web/vendor"
    pathzip = "/Users/ioedu/projects/prj_tinymarket-test/vendor.zip" 
    zipdir(pathvendor,pathzip)
    #pr("zipdir finised");die()
    jsonhlp = Json(pathconfig)
    jsonhlp.load_data()
    dicproject = jsonhlp.get_dictbykey("id",project)
    # ppr(dicproject["backend"]["prod"]); # die()
    if dicproject is None:
        pr(f"No deployed: project {project} not found")
        return 0

    # la conexión no se hace a un directorio con ruta absoluta sino que 
    # se toma la carpeta de destino como absoluta, esto es para evitar que se tenga acceso a carpetas padres
    # por lo tanto para mi "/" seria equivalente a $HOME
    dicaccess = dicproject["backend"]["prod"]
    # ppr(dicaccess);die("access")
    sftp = Sftpit(dicaccess)
    sftp.connect()
    if sftp.is_connected():
        sftp.upload(pathzip, "/www/dom_theframework.es/tinymarket.theframework.es/backend_web")
        sftp.close()

    ssh = Sshit(dicaccess)
    ssh.connect()
    ssh.cmd("cd $HOME/www/dom_theframework.es/tinymarket.theframework.es/backend_web")
    #ssh.cmd("rm -f vendor.zip")
    ssh.cmd("git pull")
    ssh.cmd("rm -fr vendor")
    ssh.cmd("unzip vendor.zip -d ./")
    ssh.cmd("rm -f vendor.zip")
    ssh.execute()
    ssh.close()
    pr(f"...deploy of {project} has finished")

if __name__ == "__main__":
    index("tinymarket")