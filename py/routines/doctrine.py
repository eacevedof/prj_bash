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

def replace_null(content):
    return content.replace("'NULL'","null")

def proces_entity(pathentity):
    content = file_get_contents(pathentity)
    content = replace_null(content)
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