from py.tools.tools import mkdir, scandir, get_datetime, rmdir_like, file_get_contents, file_put_contents, get_basename
from py.tools.helpers.react_crud_fields import ReactCrudFields, FIELD_REPLACES
from py.tools.helpers.react_crud_inputs import INPUTS_TPLS

PATH_MODULE = "/Users/ioedu/projects/prj_eafpos/frontend/restrict/src/modules"
FOLDER_TEMPLATE = "zzz-tpl"

MODEL_REPLACES = {
    "zzz-tpls": "app-tables",
    "zzz-tpl": "app-table",
    "zzz_tpls": "app_tables",
    "zzz_tpl": "app_table",
    "ZzzTpls": "AppTables",
    "ZzzTpl": "AppTable",
    "Tpls": "Tables",
    "Tpl": "Table",
    "tpls": "tables",
    "tpl": "table"
}

def remdir_old():
    pathlike = f"{PATH_MODULE}/20210*"
    rmdir_like(pathlike)

class ReactCrud:

    def __init__(self, table, metadada):
        remdir_old()
        tablemid = table.replace("_", "-")
        time = get_datetime()
        self.__tmp_folder = f"{time}_{tablemid}"
        self.__table = table
        self.__fields = ReactCrudFields(metadada)

    def __create_temp_dir(self):
        path = f"{PATH_MODULE}/{self.__tmp_folder}"
        self.__mod_folder = path
        mkdir(path)

    def __save_replaced(self, path_from: str, path_to: str):
        content = file_get_contents(path_from)
        content = self.__get_replaced_model(content)
        file_put_contents(path_to, content)

    def __save_replaced_views(self, path_from: str, path_to: str) -> str:
        content = file_get_contents(path_from)
        content = self.__get_replaced_model(content)

        content = self.__get_replaced_fields(content)
        view_name = get_basename(path_to).replace(".js","")
        strinput = self.__fields.get_inputs(view_name=view_name)
        content = self.__get_replaced_inputs(content, strinput)

        file_put_contents(path_to, content)

    def __root_folder(self):
        path_from = f"{PATH_MODULE}/{FOLDER_TEMPLATE}"
        path_to = f"{PATH_MODULE}/{self.__tmp_folder}"

        mkdir(path_to)
        files = scandir(path_from)

        for strfile in files:
            if ".js" not in strfile:
                continue
            strfileto = self.__get_replaced_model(strfile)
            self.__save_replaced(f"{path_from}/{strfile}", f"{path_to}/{strfileto}")

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
            self.__save_replaced_views(f"{path_from}/{strfile}", f"{path_to}/{strfile}")

    def __get_replaced_model(self, content: str) -> str:
        for tag in MODEL_REPLACES:
            value = MODEL_REPLACES[tag]
            content = content.replace(tag, value)
        return content

    def __get_replaced_fields(self, content: str) -> str:
        for field_tag in FIELD_REPLACES:
            strfields = self.__fields.get(tag_name=field_tag)
            field_tag = f"//%{field_tag}%"
            content = content.replace(field_tag, strfields)
        return content

    def __get_replaced_inputs(self, content: str, strinputs: str) -> str:
        for form_tag in INPUTS_TPLS:
            form_tag = f"%{form_tag}%"
            content = content.replace(form_tag, strinputs)
        return content

    def run(self):
        self.__create_temp_dir()
        self.__root_folder()
        self.__async_folder()
        self.__async_queries_folder()
        self.__config_folder()
        self.__views_folder()

