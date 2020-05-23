# tools.tools.py
import sys
import os
import json
from pprint import pprint

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

def file_get_contents(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        return f"no file found: {filename}"

def file_put_contents(filename,strdata=""):
    try:
        with open(filename, 'w') as f:
            f.write(strdata)
    except IOError:
        return f"no file found: {filename}"

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

def is_file(pathfile):
    from os import path
    return path.exists(pathfile)

def is_idr(pathdir):
    return os.path.isdir(path)

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


def get_realpath(path):
    return os.path.realpath(path)

def get_path_config_json():
    pathdir = get_dir(__file__)
    pathjson = pathdir+"/../config/projects.local.json"
    pathconfig = get_realpath(pathjson)
    return pathconfig

class Json:
    
    def __init__(self, pathfile=""):
        self.pathfile = pathfile
        self.data = []

    def load_data(self):
        # print(self.pathfile)
        # sys.exit()
        with open(self.pathfile) as jfile:
            self.data = json.load(jfile)

    def get_loaded(self):
        self.load_data()
        return self.data

    def set_pathfile(self,pathfile):
        self.pathfile = pathfile

    def get_dictbykey(self,k,v):
        for objdict in self.data:
            for key in objdict:
                if(key == k and objdict[key]==v):
                    return objdict
        return None

    def get_data(self):
        return self.data

    def reset(self):
        self.pathfile = ""
        self.data = []