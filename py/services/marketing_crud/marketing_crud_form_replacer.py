from typing import List
from py.services.marketing_crud.marketing_crud_config import FORM_REPLACES, INPUTS_TPLS

class MarketingCrudFormReplacer:

    def __init__(self, metadada):
        self.__metadata = metadada
        self.__load_replaces()

    def __load_replaces(self):
        self.__replaces = {
            "FORM_CLONE": self.__get_content("FORM_CLONE"),
            "FORM_DELETE": self.__get_content("FORM_DELETE"),
            "FORM_DELETELOGIC": self.__get_content("FORM_DELETELOGIC"),
            "FORM_DETAIL": self.__get_content("FORM_CLONE"),
            "FORM_INSERT": self.__get_content("FORM_INSERT"),
            "FORM_UPDATE": self.__get_content("FORM_UPDATE"),
        }

    def __get_not_excluded(self, form_tag: str):
        exclude = FORM_REPLACES[form_tag]["exclude"]
        fields = []
        for row in self.__metadata:
            field_name = row["field_name"]
            if not field_name in exclude:
                fields.append(row)
        return fields

    def __get_content(self, form_tag: str):
        fields = self.__get_not_excluded(form_tag)
        html = INPUTS_TPLS[form_tag]["html"]

        result = []
        for field_data in fields:
            field_name = field_data["field_name"]
            new_html = html.replace(f"%field_name%",field_name)
            result.append(new_html)

        return "\n".join(result)

    def get_replaced(self, content) -> str:
        for form_tag in self.__replaces:
            str_value = self.__replaces[form_tag]
            form_tag = f"%{form_tag}%"
            content = content.replace(form_tag, str_value)
        return content
        


