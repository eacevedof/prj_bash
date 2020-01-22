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

def get_newname(filename,arversion):
    parts = filename.split(".")
    #parts = parts[0] + [".".join(arversion)] + parts[1]
    parts.insert(1,".".join(arversion))
    # parts.insert(2,)
    newname = "_".join(parts)
    
    return newname

def index(project):
    pathprj = "/Users/ioedu/projects"
    pathdumps = "/Users/ioedu/dockercfg/db_dumps"
    projects = {"gotit":{"filename":"db_gotit.sql","pathdump":pathprj+"/prj_gotit_b/db/"}}
    
    lastbackup = get_last_backup(projects[project]["pathdump"])
    arvers = get_version(lastbackup)
    arvers = get_increased(arvers)
    #pr(arvers)
    newname = get_newname(projects[project]["filename"],arvers)
    pr(newname,"newname")


# esto da error de importación de tools
# if __name__ == "__main__":
# index("gotit")