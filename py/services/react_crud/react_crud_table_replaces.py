from py.services.react_crud.react_crud_config import MODEL_REPLACES

class ReactCrudTableReplaces:

    def __init__(self, table):
        tablemid = table.replace("_", "-")
        self.__table = table
        self.__replaces = MODEL_REPLACES
        self.__load_model_variants()

    def __load_model_variants(self):
        table = self.__table
        
        self.__replaces["zzz-tpls"] = table.replace("_","-") + "s"
        self.__replaces["zzz-tpl"] = table.replace("_","-")
        self.__replaces["zzz_tpls"] = table + "s"
        self.__replaces["zzz_tpl"] = table
        self.__replaces["ZzzTpls"] = self.__get_camelcased(table + "s")
        self.__replaces["ZzzTpl"] = self.__get_camelcased(table)
        self.__replaces["Tpls"] = self.__get_camelcased(table.replace("app_","").replace("base_","") + "s")
        self.__replaces["Tpl"] = self.__get_camelcased(table.replace("app_","").replace("base_",""))
        self.__replaces["tpls"] = table.replace("app_","").replace("base_","") + "s"
        self.__replaces["tpl"] = table.replace("app_","").replace("base_","")

    def __get_camelcased(self, string:str):
        words = string.lower().split("_")
        ucased = []
        for word in words:
            ucased.append(word.capitalize())
        return "".join(ucased)

    def get_replaced(self, content:str) -> str:
        for table_tag in self.__replaces:
            str_value = self.__replaces[table_tag]
            content = content.replace(table_tag,str_value)
        return content
