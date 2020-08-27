# routines.reactgen.py
# py.sh reactgen <dbname> <table>

from tools.tools import is_dir, scandir, get_now, pr, mkdir, get_basename
import shutil
import os

# conectar con la bd
def get_tpl():
    tpl = {
        "pathmodule":"/Users/ioedu/projects/prj_tinymarket_front/frontend_react/restrict/src/modules/product"
    }
    return tpl


def index(db, table):
    pr(db,"db")
    pr(table,"table")
    # módulo plantilla
    dictpl = get_tpl()
    pr(dictpl)
    
