# routines.reactgen.py
# py.sh reactgen <dbname> <table>

from tools.tools import scandir, get_datetime, pr, copydir
import json
import shutil
import os
import requests

def get_token(urllogin):
    r = requests.post(urllogin, data={"user":"fulanito","password":"menganitox"}, headers={"Origin":"http://localhost:3000"})
    #return r.text
    dic = json.loads(r.text)
    if bool(dic["data"]):
        return dic["data"]["token"]
    
    pr(dic["errors"])
    return ""

def get_fields(urltable, token):
    r = requests.post(urltable, data={"apify-usertoken":token}, headers={"Origin":"http://localhost:3000"})
    dic = json.loads(r.text)
    if bool(dic["data"]):
        return dic["data"]

    pr(dic["errors"])
    return None

# conectar con la bd
def get_tpl():
    tpl = {
        "endpoint-login": "http://localhost:10000/apifiy/security/login",
        "endpoint-fields": "http://localhost:10000/apify/fields/c4/db-tinymarket/%table%",
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

    token = get_token(dictpl["endpoint-login"])
    #pr(token,"token")
    urltable = dictpl["endpoint-fields"].replace("%table%",table)
    fields = get_fields(urltable, token)

    pr(fields,"fields")

    paththemp = dictpl["pathtemp"]
    #copydir(dictpl["pathmodule"], paththemp)
    #pr(dictpl)
    files = scandir(paththemp)
    pr(files,f"files en {pathtemp}")
