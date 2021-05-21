from py.tools.tools import mkdir, scandir, get_datetime, pr, file_get_contents, file_put_contents

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

    def __sync_folder(self):
        path_from = f"{PATH_MODULE}/{FOLDER_TEMPLATE}/async"
        path_to = f"{PATH_MODULE}/{self.__tmp_folder}/async"

        mkdir(path_to)
        files = scandir(path_from)

        for strfile in files:
            if ".js" not in strfile:
                continue

            path_file_from = f"{path_from}/{strfile}"
            content = file_get_contents(path_file_from)

            path_file_to = f"{path_to}/{strfile}"
            file_put_contents(path_file_to, content)


    def run(self):
        self.__create_dir()
        self.__sync_folder()
