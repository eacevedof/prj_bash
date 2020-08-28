# routines.reactgen.py
# py.sh reactgen <dbname> <table>

from tools.tools import scandir, get_datetime, pr, copydir, file_get_contents, file_put_contents
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
        "table":"app_product"
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
        "entity": "apparray",
        "entity-singular": "App Array",
        "entity-plural": "App Arrays",
    }
    return tpl

def get_jsfiles(pathfolder):
    files = scandir(pathfolder)
    files = [file for file in files if file.find(".js")!=-1]
    return files


def replace_in_file(pathfile, dicfr={}):
    if not bool(dicfr):
        return 

    content = file_get_contents(pathfile)
    for k in dicfr:
        content = content.replace(k, dicfr[k])
    file_put_contents(pathfile, content)



def replace_queries(pathfolder, dicfrom, dicto):
    if not is_dir(pathfolder)
        return 

    files = get_jsfiles(pathfolder)
    dicmerge = {}
    for k in dicfrom:
        if dicto.get(k):
            dicmerge[dicfrom[k]] = dicto[k]

    for file in files:
        pathfile = pathfolder.c
    


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
