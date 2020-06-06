# routines.fromserver.py

"""
descarga recursos de produccion

ejemplo:
    py.sh fromserver tinymarket
"""
from tools.tools import *
from tools.sftpit import Sftpit

def index(project):
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
        dbfile = dicproject["db"]["dblocal"]
        dbfile = f"{dbfile}_{now}.sql"

        cmd = f"cd backup_bd; mi_mysqldump --no-tablespaces --host={host} --user={user} --password={password} {database} > {dbfile}"
        sftp.execute(cmd)
        pathto = dicproject["db"]["pathyog"]+"/"+dbfile
        pathfrom = f"backup_bd/{dbfile}"
        sftp.download(pathfrom, pathto)
        sftp.close()
