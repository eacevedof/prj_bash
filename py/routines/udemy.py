# routines.udemy.py
import sys
from pprint import pprint

def pd(var,title=""):
    if title!="":
        print(title)
    print(var)
    sys.exit()

def file_get_contents(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        return f"no file found: {filename}"

def get_numberpos(arlines):
    arnumlines = []
    for ipos, strline in enumerate(arlines):
        if strline[0].isdigit() and strline.find(" min")!=-1:
            arnumlines.append(ipos)
    return arnumlines


def get_titles_pos(arclean):
    arpostitl = []
    for ipos, strline in enumerate(arclean):
        # si empieza por numero y no tiene la palabra min
        if strline[0].isdigit() and strline.find(" min")!=-1:
            arpostitl.append(ipos)
    return arpostitl

def get_title_w_min(ipostitle,arpostitl,arclean):
    idxtitl = arpostitl.index(ipostitle)
    pd(idxtitl,"idxtitle")
    iend = arpostitl[idxtitl+1]
    arconcat = []
    for strline in arclean[ipostitle:iend]:
        arconcat.append(strline)
    strtitle = " ".join[arconcat]
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
        print(f"{i} {ipostitle}")
        strtitle = get_title_w_min(ipostitle, arpostitl, arclean)
        






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
        