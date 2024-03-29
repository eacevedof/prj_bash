from py.tools.tools import mkdir, scandir, get_datetime, rmdir_like, file_get_contents, file_put_contents, get_basename
from py.services.marketing_crud.marketing_crud_config import \
    PATH_MODULE, FOLDER_TEMPLATE
from py.services.marketing_crud.marketing_crud_fields_replacer import MarketingCrudFieldsReplacer
from py.services.marketing_crud.marketing_crud_table_replaces import MarketingCrudTableReplaces
from py.services.marketing_crud.marketing_crud_form_replacer import MarketingCrudFormReplacer

def remdir_old():
    pathlike = f"{PATH_MODULE}/20210*"
    rmdir_like(pathlike)


class MarketingCrud:

    def __init__(self, table, metadada):
        remdir_old()
        tablemid = table.replace("_", "-")
        time = get_datetime()
        self.__tmp_folder = f"{time}_{tablemid}"

        self.__table_replacer = MarketingCrudTableReplaces(table)
        self.__fields_replacer = MarketingCrudFieldsReplacer(metadada)
        self.__form_replacer = MarketingCrudFormReplacer(metadada)


    def __create_temp_dir(self):
        path = f"{PATH_MODULE}/{self.__tmp_folder}"
        self.__mod_folder = path
        mkdir(path)

    def __save_replaced(self, path_from: str, path_to: str):
        content = file_get_contents(path_from)
        content = self.__get_all_replaces(content)
        file_put_contents(path_to, content)

    def __get_all_replaces(self, content) -> str:
        content = self.__table_replacer.get_replaced(content)
        content = self.__fields_replacer.get_replaced(content)
        content = self.__form_replacer.get_replaced(content)
        return content

    def __root_folder(self):
        path_from = f"{PATH_MODULE}/{FOLDER_TEMPLATE}"
        path_to = f"{PATH_MODULE}/{self.__tmp_folder}"

        mkdir(path_to)
        files = scandir(path_from)

        for strfile in files:
            if ".js" not in strfile:
                continue
            self.__save_replaced(f"{path_from}/{strfile}", f"{path_to}/{strfile}")

    def __async_folder(self):
        path_from = f"{PATH_MODULE}/{FOLDER_TEMPLATE}/async"
        path_to = f"{PATH_MODULE}/{self.__tmp_folder}/async"

        mkdir(path_to)
        files = scandir(path_from)

        for strfile in files:
            if ".js" not in strfile:
                continue
            self.__save_replaced(f"{path_from}/{strfile}", f"{path_to}/{strfile}")

    def __async_queries_folder(self):
        path_from = f"{PATH_MODULE}/{FOLDER_TEMPLATE}/async/queries"
        path_to = f"{PATH_MODULE}/{self.__tmp_folder}/async/queries"

        mkdir(path_to)
        files = scandir(path_from)

        for strfile in files:
            if ".js" not in strfile:
                continue
            self.__save_replaced(f"{path_from}/{strfile}", f"{path_to}/{strfile}")

    def __config_folder(self):
        path_from = f"{PATH_MODULE}/{FOLDER_TEMPLATE}/config"
        path_to = f"{PATH_MODULE}/{self.__tmp_folder}/config"

        mkdir(path_to)
        files = scandir(path_from)

        for strfile in files:
            if ".js" not in strfile:
                continue
            self.__save_replaced(f"{path_from}/{strfile}", f"{path_to}/{strfile}")

    def __views_folder(self):
        path_from = f"{PATH_MODULE}/{FOLDER_TEMPLATE}/views"
        path_to = f"{PATH_MODULE}/{self.__tmp_folder}/views"

        mkdir(path_to)
        files = scandir(path_from)

        for strfile in files:
            self.__save_replaced(f"{path_from}/{strfile}", f"{path_to}/{strfile}")

    def run(self):
        self.__create_temp_dir()
        self.__root_folder()
        self.__async_folder()
        self.__async_queries_folder()
        self.__config_folder()
        self.__views_folder()

