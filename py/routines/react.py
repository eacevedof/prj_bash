# routines.react.py
print("routines.react.py")
from tools.tools import file_get_contents,pr,pd,file_put_contents

# obtengo el contenido el archivo de configuracion .pysh
def get_pysh_lines(pathfile):
    strcont = file_get_contents(pathfile)
    arlines = strcont.split("\n")
    return arlines

def get_pysh_dict(arlines):
    configdic = []
    for line in arlines:
        artemp = line.split("=")
        print(artemp[0])
        print(artemp[1])
        configdic.append({artemp[0]:artemp[1]})
    return configdic

def get_config(pathfile):
    arlines = get_pysh_lines(pathfile)
    diconfig = get_pysh_dict(arlines)
    return diconfig

def index(pathfile):
    config = get_config(pathfile)

    print(config)
 


    
    # obtener la configuracion de .pysh
    # copiar contenido de PATH_BUILD a PATH_PUBLIC
        # no copiar el index.html
    # cambiar el nombre de asset-manifest.json a manifest.json
    # copiar el contenido de index.html en PATH_INDEX_TWIG