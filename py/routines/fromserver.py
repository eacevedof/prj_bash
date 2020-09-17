# routines.fromserver.py

"""
descarga recursos de produccion

ejemplo:
    py.sh fromserver.database tinymarket
"""
from tools.tools import *
from tools.sftpit import Sftpit

def database(project):
    dicproject = get_dicconfig(project)
    # ppr(dicproject);
    dicaccess = dicproject["backend"]["prod"]
    # pd(dicaccess);
    sftp = Sftpit(dicaccess)
    sftp.connect()
    if sftp.is_connected():
        host = dicproject["db"]["prod"]["server"]
        user = dicproject["db"]["prod"]["user"]
        password = dicproject["db"]["prod"]["password"]
        database = dicproject["db"]["prod"]["database"]
        now = get_datetime()
        dblocal = dicproject["db"]["dblocal"]
        dbfile = f"{dblocal}_{now}.sql"

        cmd = f"cd backup_bd; mysqldump --no-tablespaces --host={host} --user={user} --password={password} {database} > {dbfile}"
        sftp.execute(cmd)
        pathfrom = f"backup_bd/{dbfile}"
        pathto = dicproject["db"]["pathyog"]+"/prod_"+dbfile

        sftp.download(pathfrom, pathto)
        sftp.close()
        pathreplacer = get_realpath(get_dir(__file__)+"/../tools/replacer.py")

        cmd = f"python {pathreplacer} {database} {dblocal} {pathto}"
        sh(cmd)

def download(pathfom):
    if not pathfom:
        return "No pathfrom provided"

    project = "eduardoaf"
    dicproject = get_dicconfig(project)
    dicaccess = dicproject["backend"]["prod"]
    # pd(dicaccess);
    sftp = Sftpit(dicaccess)
    sftp.connect()
    if sftp.is_connected():
        print("downloading: \n"+pathfom)
        host = dicproject["db"]["prod"]["server"]
        user = dicproject["db"]["prod"]["user"]
        password = dicproject["db"]["prod"]["password"]
        database = dicproject["db"]["prod"]["database"]
        
        filename = get_basename(pathfom)
        pathto = dicproject["db"]["pathyog"]+"/"+filename

        sftp.download(pathfom, pathto)
        sftp.close()
        print(f"download process finished in path: {pathto}")
        