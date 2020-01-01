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

def get_title_w_min(ipostitle,arpostitl,arclean):
    pr(arpostitl,"getwmin: arpostitl")
    pr(arclean,"getwmin: arclean")
    pr(ipostitle,"getwmin: ipostitle")
    idx = arpostitl.index(ipostitle)

    
    # pr(idx,"idx")
    iend = arpostitl[idx+1]
    pr(iend,"iend")
    arconcat = []
    for i, strline in enumerate(arclean):
        if(i>=ipostitle and i<=iend):
            arconcat.append(strline)
    #pd(arconcat,"arconcat")
    strtitle = " ".join(arconcat)
    return strtitle

def index(pathfile):
    strcont = file_get_contents(pathfile)
    arlines = strcont.split("\n")
    # quito lineas en blanco
    arclean = list(filter(lambda strline: strline.strip()!="", arlines))
    # pprint(arclean)
    arpostitl = get_titles_pos(arclean)
    # pprint(arpostitl)
    for i, ipostitle in enumerate(arpostitl):
        # print(f"{i} {ipostitle}")
        strtitle = get_title_w_min(ipostitle, arpostitl, arclean)
        pr(strtitle,"strtitle")






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
        