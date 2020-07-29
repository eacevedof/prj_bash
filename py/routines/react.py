# routines.react.py
# py.sh "/Users/ioedu/projects/prj_doblerr/frontend_react/pannel/.pysh" index react
print("routines.react.py")
from tools.tools import file_get_contents,pr,pd,file_put_contents,is_dir
import shutil
import os

# obtengo el contenido el archivo de configuracion .pysh
def get_pysh_lines(pathfile):
    strcont = file_get_contents(pathfile)
    arlines = strcont.split("\n")
    return arlines

def get_pysh_dict(arlines):
    configdic = []
    for line in arlines:
        artemp = line.split("=")
        # print(artemp[0])
        # print(artemp[1])
        configdic.append({artemp[0]:artemp[1]})
    return configdic

def get_config(pathfile):
    arlines = get_pysh_lines(pathfile)
    diconfig = get_pysh_dict(arlines)
    return diconfig

def get_key(config,key):
    for cfg in config:
        if key in cfg:
            return cfg[key]
    return ""

def index(pathfile):
    config = get_config(pathfile)
    # print(config)
    pathbuild = get_key(config,"PATH_BUILD")
    pathpublic = get_key(config,"PATH_PUBLIC")
    pathcache = get_key(config,"PATH_CACHE")
    pathtwig = get_key(config,"PATH_INDEX_TWIG")

    if pathpublic!="":
        print("...removing pathpublic: "+pathpublic)
        shutil.rmtree(pathpublic)

        if pathbuild!="":
            print("...copying pathbuild: "+pathbuild)
            shutil.copytree(pathbuild, pathpublic)

    if pathpublic!="":
        print("...removing index.html")
        os.remove(pathpublic+"/index.html")

    if pathtwig!="" and pathbuild != "":
        print("...copying index.html to twig: "+pathtwig)
        shutil.copyfile(pathbuild+"/index.html", pathtwig)

    if pathcache!="" and is_dir(pathcache):
        print("...removing cache")
        shutil.rmtree(pathcache)
    
    print(f"\npy.sh react {pathfile} \n\t- process finished!")

    # obtener la configuracion de .pysh
    # copiar contenido de PATH_BUILD a PATH_PUBLIC
        # no copiar el index.html
    # cambiar el nombre de asset-manifest.json a manifest.json
    # copiar el contenido de index.html en PATH_INDEX_TWIG