# routines.reactgen.py
# py.sh reactgen <dbname> <table>

from tools.tools import scandir, get_datetime, pr, copydir
import shutil
import os

def get_token():
    pass
# conectar con la bd
def get_tpl():
    tpl = {
        "endpoint-login": "http://localhost:10000/apifiy/security/login"
        "endpoint-fields": "http://localhost:10000/apify/fields/c4/db-tinymarket/%table%"
        "pathmodule" : "/Users/ioedu/projects/prj_tinymarket_front/frontend_react/restrict/src/modules/product",
        "entity": "product",
        "entity-singular": "Product",
        "entity-plural": "Products",
    }
    h, t = os.path.split(tpl["pathmodule"])
    now = get_datetime()
    tpl["pathtemp"] = f"{h}/{now}"
    return tpl

def get_dest():
    tpl = {
        "entity": "product",
        "entity-singular": "Product",
        "entity-plural": "Prooducts",
    }
    return tpl


def index(table):
    # módulo plantilla
    dictpl = get_tpl()
    pr(dictpl,"dictpl")

    paththemp = dictpl["pathtemp"]
    copydir(dictpl["pathmodule"], paththemp)
    #pr(dictpl)
    files = scandir(paththemp)
    pr(files,f"files en {pathtemp}")
