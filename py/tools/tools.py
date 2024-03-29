# tools.tools.py
import sys
import os
from .json import Json
from pprint import pprint
from datetime import datetime
import ntpath

PATH_PROJECTS_JSON = "config/projects.local.json"

def printx(mxvar):
    if isinstance(mxvar,list):
        for i, item in enumerate(mxvar):
            print(i," => ",item)
    else:
        print(mxvar)

def pr(var,title=""):
    if title!="":
        print(title)
    printx(var)

def ppr(var,title=""):
    if title!="":
        print(title)
    pprint(var)    

def pd(var,title=""):
    if title!="":
        print(title)
    printx(var)
    sys.exit()

def die():
    sys.exit()

def file_get_contents(pathfile):
    try:
        with open(pathfile) as f:
            return f.read()
    except IOError:
        return f"no file found: {pathfile}"

def file_put_contents(pathfile, strdata=""):
    try:
        with open(pathfile, 'w') as f:
            f.write(strdata)
    except IOError:
        return f"no file found: {pathfile}"

def get_datetime():
    from datetime import datetime
    now = datetime.now()
    now.strftime("%Y-%m-%d %H:%M:%S")
    # pr(now)
    now = str(now).replace("-","").replace(":","").replace(" ","")
    now = now[:-7]
    return now

def copyf(path1,path2):
    from os import path
    from shutil import copyfile

    if not path.exists(path1):
        return 0

    if not path.exists(path2):
        copyfile(path1, path2)
        return 1
    
    return 0

def copydir(path1, path2):
    from os import path
    from shutil import copytree    
    
    if not path.exists(path1):
        return 0

    if not path.exists(path2):
        copytree(path1, path2)
        return 1
    
    return 0

def is_file(pathfile):
    from os import path
    return path.exists(pathfile)

def is_dir(pathdir):
    return os.path.isdir(pathdir)

def die(text=""):
    import sys
    if text!="" :print(text)
    sys.exit()

def get_dir(path):
    realpath = os.path.dirname(os.path.realpath(path))
    return realpath

def get_basename(path,ext=1):
    import ntpath
    basename = ntpath.basename(path)
    #print(basename); die("basename")
    if ext==1:
        return basename
    parts = basename.split(".")
    del parts[-1]
    basename = ".".join(parts)
    return basename

def get_currdir():
    return os.getcwd()

def get_realpath(path):
    return os.path.realpath(path)

def get_path_config_json():
    pathdir = get_dir(__file__)
    pathjson = pathdir+"/../"+PATH_PROJECTS_JSON
    pathconfig = get_realpath(pathjson)
    return pathconfig

def get_now():
    now = datetime.now()
    hhmmss = now.strftime("%H:%M:%S")
    return hhmmss 

def scandir(pathfolder):
    # pr(f"pathfolder: {pathfolder}")
    # return [f for f in os.listdir(pathfolder) if os.path.isfile(f)]
    
    f = []
    for entry in os.scandir(pathfolder):
        #print(entry)
        #if entry.is_file():
        if entry.name != ".DS_Store":
            f.append(entry.name)
    return f
         
def mkdir(pathfolder):
    try:
        if not is_dir(pathfolder):
            os.mkdir(pathfolder)
    except OSError:
        print ("Creation of the directory %s failed" % pathfolder)
    else:
        print ("Successfully created the directory %s " % pathfolder)

def rmdir(pathfolder):
    from shutil import rmtree
    try:
        if not is_dir(pathfolder):
            rmtree(pathfolder)
    except OSError:
        print ("removing directory %s failed" % pathfolder)
    else:
        print ("directory %s removed successfully!" % pathfolder)

def rmdir_like(pathlike):
    cmd = f"rm -fr {pathlike}"
    sh(cmd)

def get_dicconfig(project=None):
    pathconfig = get_path_config_json()
    jsonhlp = Json(pathconfig)
    jsonhlp.load_data()
    if not project:
        return jsonhlp
    dicproject = jsonhlp.get_dictbykey("id",project)
    return dicproject


def get_basename(pathfile):
    head, tail = ntpath.split(pathfile)
    return tail or ntpath.basename(head)

def sh(strcmd):
    try:
        os.system(strcmd)
    except Exception as error:
        print(f"tools.sh: error: {error}")

def shsudo(strcmd, passw):
    try:
        # sudocmd = f"sudo -S %s"%(strcmd)
        #sudocmd = f"sudo -S {strcmd}"
        #os.popen(sudocmd,"w").write(passw)
        r = os.system('echo %s|sudo -S %s' % (passw, strcmd))
        # pr(r,"sudo result")

    except Exception as error:
        print(f"tools.sh: error: {error}")

