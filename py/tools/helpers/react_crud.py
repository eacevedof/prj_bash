from py.tools.tools import mkdir, scandir, get_datetime

PATH_MODULE = "/Users/ioedu/projects/prj_eafpos/frontend/restrict/src/modules"
FOLDER_TEMPLATE = "zzz-tpl"
TAG_TABLE = "%table%"
TAG_ALIAS = "%alias%"
TAG_WITHOUT_PREFIX = "%withoutprefix%"
SYS_FIELDS = [

]

class ReactCrud:

    def __init__(self, table, metadada):
        time = get_datetime()
        self.__tmp_folder = f"{time}_{table}"
        self.__table = table
        self.__metadata = metadada

    def __create_dir(self):
        path = f"{PATH_MODULE}/{self.__tmp_folder}"
        self.__mod_folder = path
        mkdir(path)

    def __replace_async(self):
        path = f"{PATH_MODULE}/{FOLDER_TEMPLATE}/async"
        scandir(path)

    def run(self):
        self.__create_dir()
        self.__replace_async()
