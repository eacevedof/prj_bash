# routines.udemy.py
from pprint import pprint

def file_get_contents(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        return f"no file found: {filename}"

def get_numberpos(arlines):
    arnumlines = []
    for ipos,strline in arlines:
        if strline[0].isdigit():
            arnumlines.append(ipos)
    return arnumlines

def index(pathfile):
    strcont = file_get_contents(pathfile)
    arlines = strcont.split("\n")
    arclean = list(filter(lambda strline: strline.strip()!="", arlines))
    # si empiezan por numero son lineas de capitulos y minutos, el primero seria el min de seccion
    arcapits = list(filter(lambda strline: strline[0].isdigit(),arclean))
    arcapits = arclean
    # del arcapits[0]
    pprint(arcapits)

    newar = []
    for ipos, strline in enumerate(arcapits):
        if strline.find(" min")!=-1:
            # print(strline)
            newar.append(f"{arcapits[ipos-1]} {strline}")
    
    print(newar)
        