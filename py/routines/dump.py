# routines.dump.py

"""
mueve datos de la carpeta mapeada del contenedor de sqlyog a un proyecto concreto
hay que configurar el diccionario projects
"""

import sys
import os
import numpy as np
from tools.tools import file_get_contents,pr,pd,file_put_contents,get_datetime,copyf,die,is_file


def get_last_backup(path):
    files = []
    for entry in os.scandir(path):
        if entry.name!=".DS_Store":
            files.append(entry.name)

    if not files:
        return ""

    files.sort()
    # print(files)
    return files[-1]


def get_version(filename):
    if not filename:
        return []

    parts = filename.split("_")
    # pr(parts,"parts")
    lastone = parts[-1].replace(".sql","")
    #pr(lastone)
    # v1,v2,v3 = lastone.split(".")
    return lastone.split(".")


def get_increased(arversion, type="minor"):
    if not arversion:
        return ["1","0","0"]

    for i in range(len(arversion)):
        if i==2:
            vx = int(arversion[i])
            vx += 1
            arversion[i] = str(vx)
    return arversion


def is_equal(path1, path2):
    from os import path
    import filecmp 
    
    if not path.exists(path1):
        return False
    
    if not path.exists(path2):
        return False

    isok = filecmp.cmp(path1,path2)
    return isok


def get_newname(filename,arversion):
    parts = filename.split(".")
    #parts = parts[0] + [".".join(arversion)] + parts[1]
    #parts.insert(1,".".join(arversion))
    parts.insert(1,get_datetime())
    newname = "_".join(parts)
    i = newname.rfind("_")
    newname = newname[:i] + "." + newname[i+1:]
    return newname


def index(project):
    #Ejemplo: py.sh tinymarket index dump
    pathprj = "/Users/ioedu/projects"
    pathdumps = "/Users/ioedu/dockercfg/db_dumps"
    projects = {
            "gotit":{"filename":"db_gotit.sql","pathdump":pathprj+"/prj_gotit_b/db/"},
            "tinymarket":{"filename":"db_tinymarket.sql","pathdump":pathprj+"/prj_tinymarket/backend_web/db/","dbprod":"dbs433055"}
        }
    
    if not project in projects:
        pr(f"project {project} not found","Not copied!")
        return 0

    lastbackup = get_last_backup(projects[project]["pathdump"])
    # print(lastbackup); return 0
    filelastbk = projects[project]["pathdump"]+lastbackup
    filedump = pathdumps + "/" + projects[project]["filename"]
    
    if not is_file(filedump):
        pr(f"file: dump: {filedump} does not exist","Not copied!")
        return 0

    # pr(filelastbk,"filelastbk")
    # pr(filedump,"filedump")
    if is_equal(filedump,filelastbk):
        pr(f"files: dump: {filedump} and bk: {filelastbk} are the same","Not copied!")
        return 0

    arvers = get_version(lastbackup)
    arvers = get_increased(arvers)
    # pr(projects[project]["pathdump"]);die()
    # pr(projects[project]["filename"]); #die()
    # pr(arvers); #die()
    newname = get_newname(projects[project]["filename"],arvers)
    # pr(newname); die();
    newbackup =  projects[project]["pathdump"] + newname

    i = copyf(filedump,newbackup)
    if i==1:
        pr(f"backup copied into: {newbackup}")
    else:
        pr(f"come error ocurred copying {filedump}")
# esto da error de importación de tools
# if __name__ == "__main__":
# index("gotit")