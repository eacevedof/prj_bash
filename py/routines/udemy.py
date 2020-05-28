# routines.udemy.py
"""
py.sh udemy "/Users/ioedu/Desktop/temp.php"
py.sh udemy.index "/Users/ioedu/Desktop/temp.php"
"""

from tools.tools import file_get_contents,pr,pd,file_put_contents

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
    pr("\n - BEGIN - \n\n")
    strcont = file_get_contents(pathfile)
    arlines = strcont.split("\n")
    # quito lineas en blanco
    arclean = list(filter(lambda strline: strline.strip()!="", arlines))
    #pr(arclean,"arclean")
    arpostitl = get_titles_pos(arclean)
    #pr(arpostitl,"arpostitle")

    artitles = []
    # trato el titulo de sección
    imin = arpostitl[0]
    artitles.append(" ".join(arclean[0:imin]))
    
    for ipostitle in arpostitl:
        strtitle = get_title_min(ipostitle, arpostitl, arclean)
        artitles.append(strtitle)

    # pr(artitles,"artitles")
    artagged = []
    for i,title in enumerate(artitles):
        if(i>0):
            artagged.append(f"### [{title}]()")
            artagged.append("- ")
        else:
            artagged.append(f"### {title}")

    # pr(artagged,"artagged")
    newfile = f"{pathfile}.bk"
    strcontent = "\n".join(artagged)
    pr(strcontent)
    file_put_contents(newfile,strcontent)
    pr("\n - END - \n")