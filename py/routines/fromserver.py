# routines.fromserver.py

"""
descarga recursos de produccion

ejemplo:
    py.sh fromserver.database tinymarket
"""
from py.tools.tools import *
from py.tools.sftpit import Sftpit

def database(project):
    dicproject = get_dicconfig(project)
    # ppr(dicproject);
    dicaccess = dicproject["db"]["remote"]["ssh"]
    # pd(dicaccess);
    sftp = Sftpit(dicaccess)
    sftp.connect()
    if sftp.is_connected():
        db_remote = dicproject["db"]["remote"]
        host = db_remote["server"]
        user = db_remote["user"]
        password = db_remote["password"]
        database = db_remote["database"]

        db_local = dicproject["db"]["origin"]

        now = get_datetime()
        dblocal = db_local["database"]
        dbfile = f"{dblocal}_{now}.sql"

        cmd = f"cd backup_bd; mysqldump --no-tablespaces --host={host} --user={user} --password=\"{password}\" {database} > {dbfile}"
        sftp.execute(cmd)
        pathfrom = f"backup_bd/{dbfile}"
        pathto = db_local["pathdumps"] +"/prod_"+dbfile

        sftp.download(pathfrom, pathto)
        sftp.close()
        pathreplacer = get_realpath(get_dir(__file__)+"/../tools/replacer.py")

        cmd = f"python {pathreplacer} {database} {dblocal} {pathto}"
        sh(cmd)

# ejemplo: py.sh fromserver.download "./backup_codigo/20111008eduardoaf.com.tgz"
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

        filename = get_basename(pathfom)
        pathto = dicproject["db"]["pathyog"]+"/"+filename

        sftp.download(pathfom, pathto)
        sftp.close()
        print(f"download process finished in path: {pathto}")
