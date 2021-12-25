from typing import List
from py.services.marketing_crud.marketing_crud_config import FIELD_REPLACES, DEFAULT_VALUES_TYPES

class MarketingCrudFieldsReplacer:

    def __init__(self, metadada):
        self.__metadata = metadada
        self.__default_values_types = DEFAULT_VALUES_TYPES
        self.__load_replaces()

    def __load_replaces(self):
        self.__replaces = {
            # t.field_name
            "FIELDS_QUERY_LIST": self.__get_query_list_and_entity(FIELD_REPLACES["FIELDS_QUERY_LIST"]["exclude"]),
            "FIELDS_QUERY_ENTITY": self.__get_query_list_and_entity(FIELD_REPLACES["FIELDS_QUERY_ENTITY"]["exclude"]),

            # f"text: \"label-{field_name}\", value: \"{field_name}\""
            "FIELDS_GRID_HEADERS": self.__get_grid_headers(FIELD_REPLACES["FIELDS_GRID_HEADERS"]["exclude"]),

            # f"name: \"{field_name}\", labels: [\"label-{field_name}\"]"
            "FIELDS_FILTERCONF": self.__get_filterconf(FIELD_REPLACES["FIELDS_FILTERCONF"]["exclude"]),

            "FIELDS_CLONE": self.__get_content("FIELDS_CLONE"),
            "FIELDS_DELETE": self.__get_content("FIELDS_DELETE"),
            "FIELDS_DELETELOGIC": self.__get_content("FIELDS_DELETELOGIC"),
            "FIELDS_DETAIL": self.__get_content("FIELDS_DETAIL"),
            "FIELDS_INSERT": self.__get_content("FIELDS_INSERT"),
            "FIELDS_UPDATE": self.__get_content("FIELDS_UPDATE"),
        }

    def __get_not_excluded(self, form_tag: str) -> List:
        exclude = FIELD_REPLACES[form_tag]["exclude"]
        fields = []
        for row in self.__metadata:
            field_name = row["field_name"]
            if not field_name in exclude:
                fields.append(row)
        return fields

    def __get_content(self, form_tag: str) -> str:
        fields = self.__get_not_excluded(form_tag)

        result = []
        for row in fields:
            field_name = row["field_name"]
            field_type = row["field_type"]
            field_length = self.__get_field_length(row)
            default_value = self.__default_values_types[field_type]
            comment = f"//{field_type}({field_length})" if field_length else f"//{field_type}"
            txt = f"{field_name}: {default_value}, {comment}"
            result.append(txt)

        return "\n".join(result)


    def __get_field_length(self, field_data: dict) -> str:
        field_length = field_data.get("field_length", "")
        if not field_length:
            integers = field_data.get("ntot", "")
            if not integers:
                return ""
            decimals = field_data.get("ndec", "")
            integers = str(integers)
            decimals = str(decimals)
            field_length = integers + "," + decimals

        return field_length

    def __get_query_list_and_entity(self, excluded) -> str:
        result = []
        for field_data in self.__metadata:
            field_name = field_data["field_name"]
            if field_name in excluded:
                continue
            result.append(f"\"t.{field_name}\"")
        return ",\n".join(result)

    def __get_grid_headers(self, excluded) -> str:
        # { text: 'Code', value: 'code_erp' },
        result = []
        for field_data in self.__metadata:
            field_name = field_data["field_name"]
            if field_name in excluded:
                continue
            inner = f"text: \"label-{field_name}\", value: \"{field_name}\""
            inner = "{"+inner+"}"
            result.append(inner)
        return ",\n".join(result)

    def __get_filterconf(self, excluded) -> str:
        # {name: "id", labels:["n","n","id"]},
        result = []
        for field_data in self.__metadata:
            field_name = field_data["field_name"]
            if field_name in excluded:
                continue
            inner = f"name: \"{field_name}\", labels: [\"label-{field_name}\"]"
            inner = "{"+inner+"}"
            result.append(inner)
        return ",\n".join(result)

    def get_replaced(self, content:str) -> str:
        for field_tag in self.__replaces:
            str_value = self.__replaces[field_tag]
            # //%FIELDS_DELETE%
            content = content.replace(f"//%{field_tag}%",str_value)
        return content
