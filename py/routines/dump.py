# routines.dump.py

"""
mueve datos de la carpeta mapeada del contenedor de sqlyog a un proyecto concreto
hay que configurar el diccionario projects

ejemplo:
    py.sh dump tinymarket
"""

import os
from tools.tools import *


def get_last_backup(path):
    # pr(path);die()
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
    # db_<project>_<timestamp>.sql
    if not filename:
        return []

    parts = filename.split("_")
    # pr(parts,"parts")
    lastone = parts[-1].replace(".sql","")
    # pr(lastone); die()
    # v1,v2,v3 = lastone.split(".")
    # pr(lastone.split("."));die()
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


def get_newname(filename):
    parts = filename.split(".")
    #parts = parts[0] + [".".join(arversion)] + parts[1]
    #parts.insert(1,".".join(arversion))
    parts.insert(1,get_datetime())
    newname = "_".join(parts)
    i = newname.rfind("_")
    newname = newname[:i] + "." + newname[i+1:]
    return newname


def index(project):
    dicproject = get_dicconfig(project)
    
    if dicproject is None:
        pr(f"project {project} not found","Not copied!")
        return 0

    pathdump = dicproject["db"]["pathdump"]
    lastbackup = get_last_backup(pathdump)
    # print(">"+lastbackup); return 0
    if not lastbackup:
        lastbackup = dicproject["db"]["filename"]

    filelastbk = pathdump+"/"+lastbackup
    filedump = dicproject["db"]["pathyog"]+"/"+ dicproject["db"]["filename"]
    
    if not is_file(filedump):
        pr(f"file: dump: {filedump} does not exist","Not copied!")
        return 0

    # pr(filelastbk,"filelastbk")
    # pr(filedump,"filedump")
    if is_equal(filedump,filelastbk):
        pr(f"files: dump: {filedump} and bk: {filelastbk} are the same","Not copied!")
        return 0

    # arvers es para archivos db_<project>_<v.x.y.z>.sql
    #arvers = get_version(lastbackup)
    #arvers = get_increased(arvers)
    # pr(dicproject["pathdump"]);die()
    # pr(dicproject["filename"]); #die()
    # pr(arvers); #die()
    #newname = get_newname(dicproject["filename"],arvers)
    newname = get_newname(dicproject["db"]["filename"])
    # pr(newname); die();
    newbackup =  pathdump +"/"+ newname

    i = copyf(filedump,newbackup)
    if i==1:
        pr(f"backup copied into: {newbackup}")
        sh(f"cd {pathdump}; git add .; git commit -m 'dump.py: db {newname}'; git push;")
        pr(f"db pushed to repo")
    else:
        pr(f"some error ocurred copying {filedump}")
        return 0

    # esto lo comento porque sino el hash siempre sería distinto en is_equal(...)

    #dbprod = {dicproject["db"]["dbprod"]}
    #pr(f"...updating dbprod:{dbprod}")
    #dumpcontent = file_get_contents(newbackup)
    #dumpcontent = dumpcontent.replace(dicproject["db"]["dblocal"],dicproject["db"]["dbprod"])
    #file_put_contents(newbackup,dumpcontent)
    pr("process finished!")

# esto da error de importación de tools
# if __name__ == "__main__":
# index("gotit")
