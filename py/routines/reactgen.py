# routines.reactgen.py
# py.sh reactgen <dbname> <table>

from tools.tools import scandir, get_datetime, pr, copydir
import shutil
import os

# conectar con la bd
def get_tpl():
    tpl = {
        "pathmodule":"/Users/ioedu/projects/prj_tinymarket_front/frontend_react/restrict/src/modules/product"
    }
    h, t = os.path.split(tpl["pathmodule"])
    now = get_datetime()
    tpl["pathtemp"] = f"{h}/{now}"
    return tpl


def index(db, table):
    # módulo plantilla
    dictpl = get_tpl()
    pr(dictpl,"dictpl")

    paththemp = dictpl["pathtemp"]
    copydir(dictpl["pathmodule"], paththemp)
    #pr(dictpl)
    files = scandir(paththemp)
    pr(files,f"files en {pathtemp}")
