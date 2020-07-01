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


def index(pathentities):
    pr(f"doctrine.py path={pathentities}")
    files = get_files(pathentities)
    ppr(files)

    pr("process finished!")
# esto da error de importación de tools
# if __name__ == "__main__":
# index("gotit")