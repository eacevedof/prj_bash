from py.tools.tools import mkdir, scandir, get_datetime, rmdir_like, file_get_contents, file_put_contents, get_basename
from py.services.react_crud.react_crud_config import INPUTS_TPLS, FIELD_REPLACES, \
    PATH_MODULE, MODEL_REPLACES, FOLDER_TEMPLATE
from py.services.react_crud.react_crud_fields import ReactCrudFields


def remdir_old():
    pathlike = f"{PATH_MODULE}/20210*"
    rmdir_like(pathlike)

def get_camelcased(string):
    words = string.lower().split("_")
    ucased = []
    for word in words:
        ucased.append(word.capitalize())
    return "".join(ucased)

class ReactCrud:

    def __init__(self, table, metadada):
        remdir_old()
        tablemid = table.replace("_", "-")
        time = get_datetime()
        self.__tmp_folder = f"{time}_{tablemid}"
        self.__table = table
        self.__load_model_variants()
        self.__fields = ReactCrudFields(metadada)

    def __load_model_variants(self):
        table = self.__table
        MODEL_REPLACES["zzz-tpls"] = table.replace("_","-") + "s"
        MODEL_REPLACES["zzz-tpl"] = table.replace("_","-")
        MODEL_REPLACES["zzz_tpls"] = table + "s"
        MODEL_REPLACES["zzz_tpl"] = table
        MODEL_REPLACES["ZzzTpls"] = get_camelcased(table + "s")
        MODEL_REPLACES["ZzzTpl"] = get_camelcased(table)
        MODEL_REPLACES["Tpls"] = get_camelcased(table.replace("app_","").replace("base_","") + "s")
        MODEL_REPLACES["Tpl"] = get_camelcased(table.replace("app_","").replace("base_",""))
        MODEL_REPLACES["tpls"] = table.replace("app_","").replace("base_","") + "s"
        MODEL_REPLACES["tpl"] = table.replace("app_","").replace("base_","")

    def __create_temp_dir(self):
        path = f"{PATH_MODULE}/{self.__tmp_folder}"
        self.__mod_folder = path
        mkdir(path)

    def __save_replaced(self, path_from: str, path_to: str):
        content = file_get_contents(path_from)
        content = self.__get_replaced_model(content)

        list_replace = self.__fields.get_list_tags_replaces()
        for list_tag in list_replace:
            content = content.replace(f"//%{list_tag}%", list_replace[list_tag])

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
            strfields = self.__fields.get(field_tag=field_tag)
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

