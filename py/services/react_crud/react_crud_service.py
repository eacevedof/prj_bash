from py.tools.tools import mkdir, scandir, get_datetime, rmdir_like, file_get_contents, file_put_contents, get_basename
from py.services.react_crud.react_crud_config import INPUTS_TPLS, FIELD_REPLACES, \
    PATH_MODULE, FOLDER_TEMPLATE
from py.services.react_crud.react_crud_fields import ReactCrudFields
from py.services.react_crud.react_crud_table_replaces import ReactCrudTableReplaces

def remdir_old():
    pathlike = f"{PATH_MODULE}/20210*"
    rmdir_like(pathlike)


class ReactCrud:

# repmplazar etiqueta con valor
    def __init__(self, table, metadada):
        remdir_old()
        tablemid = table.replace("_", "-")
        time = get_datetime()
        self.__tmp_folder = f"{time}_{tablemid}"
        self.__table = table
        self.__load_model_variants()
        self.__fields = ReactCrudFields(metadada)
        self.__table_replacer = ReactCrudTableReplaces(table)

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
        return self.__table_replacer.get_replaced(content)

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

