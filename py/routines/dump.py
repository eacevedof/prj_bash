# routines.dump.py

import os
import numpy as np
from tools.tools import file_get_contents,pr,pd,file_put_contents,get_datetime


def get_last_backup(path):
    files = []
    for entry in os.scandir(path):
        files.append(entry.name)

    files.sort()
    return files[-1]


def get_version(filename):
    parts = filename.split("_")
    # pr(parts,"parts")
    lastone = parts[-1].replace(".sql","")
    #pr(lastone)
    # v1,v2,v3 = lastone.split(".")
    return lastone.split(".")


def get_increased(arversion, type="minor"):
    for i in range(len(arversion)):
        if i==2:
            vx = int(arversion[i])
            vx += 1
            arversion[i] = str(vx)
    return arversion

def is_equal(path1,path2):
    from os import path
    import filecmp 
    
    if not path.exists(path1):
        return False
    
    if not path.exists(path2):
        return False


    isok = filecmp.cmp(path1,path2)
    pr(isok,"isok")
    return isok

def get_newname(filename,arversion):
    parts = filename.split(".")
    #parts = parts[0] + [".".join(arversion)] + parts[1]
    parts.insert(1,".".join(arversion))
    parts.insert(2,get_datetime())
    newname = "_".join(parts)
    return newname

def index(project):
    pathprj = "/Users/ioedu/projects"
    pathdumps = "/Users/ioedu/dockercfg/db_dumps"
    projects = {"gotit":{"filename":"db_gotit.sql","pathdump":pathprj+"/prj_gotit_b/db/"}}
    
    if not project in projects:
        return 0


    lastbackup = get_last_backup(projects[project]["pathdump"])
    filelastbk = projects[project]["pathdump"]+lastbackup
    filedump = pathprj + "/" + projects[project]["filename"]

    pr(filelastbk,"filelastbk")
    pr(filedump,"filedump")

    if is_equal(filedump,filelastbk):
        return 0



    arvers = get_version(lastbackup)
    arvers = get_increased(arvers)
    #pr(arvers)
    newname = get_newname(projects[project]["filename"],arvers)
    pr(newname,"newname")
    punto = newname.rfind(".")
    guion = newname.rfind("_")
    pr(punto,"punto")
    pr(guion,"guion")
    
# esto da error de importación de tools
# if __name__ == "__main__":
# index("gotit")