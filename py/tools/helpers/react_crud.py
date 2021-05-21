from tools.tools import *

PATH_ROOT = "$HOME/projects/prj_eafpos/frontend/restrict/src/modules"
FOLDER_TEMPLATE = "zzz-tpl"
TAG_TABLE = "%table%"
TAG_ALIAS = "%alias%"
TAG_WITHOUT_PREFIX = "%withoutprefix%"
SYS_FIELDS = [

]

class ReactCrud:
    def __init__(self):
        pass

    def __replace_async(self):
        path = f"{PATH_ROOT}/{FOLDER_TEMPLATE}/async/"
        scandir(path)
