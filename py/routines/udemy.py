# routines.udemy.py
import sys
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

def get_titles_pos(arclean):
    arpostitl = []
    for ipos, strline in enumerate(arclean):
        # si empieza por numero y no tiene la palabra min
        if strline[0].isdigit() and strline.find(" min")==-1:
            arpostitl.append(ipos)
    return arpostitl

def get_title_min(ipostitle,arpostitl,arclean):
    idx = arpostitl.index(ipostitle)

    # si es el ultimo titulo debe llegar hasta el final de arclean
    if(idx == len(arpostitl)-1):
        iend = len(arclean)
    else:
        iend = arpostitl[idx+1]

    #pr(iend,"iend")
    arconcat = []
    for strline in arclean[ipostitle:iend]:
        arconcat.append(strline)

    strtitle = " ".join(arconcat)
    return strtitle

def index(pathfile):
    strcont = file_get_contents(pathfile)
    arlines = strcont.split("\n")
    # quito lineas en blanco
    arclean = list(filter(lambda strline: strline.strip()!="", arlines))
    pr(arclean,"arclean")
    arpostitl = get_titles_pos(arclean)
    pr(arpostitl,"arpostitle")

    artitles = []

    imin = arpostitl[0]
    artitles.append(" ".join(arclean[0:imin]))
    
    for ipostitle in arpostitl:
        strtitle = get_title_min(ipostitle, arpostitl, arclean)
        artitles.append(strtitle)

    pr(artitles,"artitles")



    pd("fin :)","FIN")



    # si empiezan por numero son lineas de capitulos y minutos, el primero seria el min de seccion
    # el problema es que no tomo en cuenta lineas con saltos
    arcapits = list(filter(lambda strline: strline[0].isdigit(),arclean))
    # arcapits = arclean
    # del arcapits[0]
    pprint(arcapits)

    newar = []
    for ipos, strline in enumerate(arcapits):
        if strline.find(" min")!=-1:
            # print(strline)
            newar.append(f"{arcapits[ipos-1]} {strline}")
    
    print(newar)
        