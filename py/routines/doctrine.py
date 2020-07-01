# routines.doctrine.py

"""
Limpia las entidades autogeneradas con doctrine usando el comando:
    php bin/console --env=local doctrine:mapping:import "App\Entity" annotation --path=src/Entity --filter="AppPromotion"

ejemplo:
    py.sh doctrine <path-entities>
    py.sh doctrine "$HOME/projects/prj_doblerr/backend_web/src/Entity"
"""

import sys
import os
from pprint import pprint
import numpy as np
from tools.tools import *

def get_files(path):
    files = scandir(path)
    entities = []
    for file in files:
        if file.find(".php") != -1:
            entities.append(file)
    return entities

def has_unused_field(strline):
    arunused = [
        "processflag","insert_platform","insert_user","insert_date","update_platform","update_user","update_date","delete_platform","delete_user","delete_date","cru_csvnote"
        ,"is_erpsent","is_enabled","i","code_erp","description","code_cache",
    ]
    for field in arunused:
        if strline.find(f"Column(name=\"{field}\", type=")!= -1:
            return True
    return False

def get_lines_to_remove(content):
    arlines = content.split("\n")
    numlines = []
    for i,strline in enumerate(arlines):
        if has_unused_field(strline):
            numlines.append(i-3)    # /**
            numlines.append(i-2)    # @var tipo
            numlines.append(i-1)    # * <en blanco>
            numlines.append(i)      # name=fieldname
            numlines.append(i+1)    # */
            numlines.append(i+2)    # private $fieldName

    distinct = set(numlines)
    unique = (list(distinct))
    return unique


def get_without_unused_fields(content):
    arremove = get_lines_to_remove(content)
    # ppr(arremove,"lines to remove")
    arlines = content.split("\n")
    rmvedlines = []
    for i,strline in enumerate(arlines):
        if i in arremove:
            continue
        rmvedlines.append(strline)
    return "\n".join(rmvedlines)

def replace_empty_comment(content):
    arlines = content.split("\n")
    rmvedlines = []
    for i,strline in enumerate(arlines):
        if strline.strip()==="*":
            continue
        rmvedlines.append(strline)
    return "\n".join(rmvedlines)    

def replace_null(content):
    return content.replace("'NULL'","null")

def replace_float(content):
    return content.replace("'0.000'","0")

def replace_singlequot(content):
    newcontent = content.replace("\\''","'")
    newcontent = newcontent.replace("'\\'","'")
    
    return newcontent

def proces_entity(pathentity):
    content = file_get_contents(pathentity)
    content = get_without_unused_fields(content)
    content = replace_empty_comment(content)
    content = replace_null(content)
    content = replace_float(content)
    content = replace_singlequot(content)
    ppr(content,f"content of: {pathentity}")


def index(pathentities):
    pr(f"doctrine.py path={pathentities}")
    entities = get_files(pathentities)
    for php in entities:
        pathentity = pathentities+"/"+php
        proces_entity(pathentity)
        die()

    pr("process finished!")
# esto da error de importación de tools
# if __name__ == "__main__":
# index("gotit")