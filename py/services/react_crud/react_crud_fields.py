from typing import List
from py.services.react_crud.react_crud_config import FIELD_REPLACES, DEFAULT_VALUES
from py.services.react_crud.react_crud_inputs import ReactCrudInputs


class ReactCrudFields:

    def __init__(self, metadada):
        self.__metadata = metadada
        self.__input = ReactCrudInputs()
        self.__default_values = DEFAULT_VALUES

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

    def __get_field_and_length(self, field_tag: str) -> List:
        fields = []
        for field_data in self.__metadata:
            field_name = field_data.get("field_name", "")
            if self.__in_excluded_by_tag(field_tag, field_name):
                continue

            field_length = self.__get_field_length(field_data)
            field_type = field_data.get("field_type", "")
            default_value = self.__default_values[field_type]

            comment = f"//{field_type}({field_length})" if field_length else f"//{field_type}"
            txt = f"{field_name}: {default_value}, {comment}"
            fields.append(txt)
        return fields

    def __in_excluded_by_tag(self, field_tag: str, field_name: str) -> bool:
        return field_name in FIELD_REPLACES[field_tag]["exclude"]

    def get(self, field_tag: str) -> str:
        fields = self.__get_field_and_length(field_tag)
        return "\n".join(fields)

    def get_inputs(self, view_name: str) -> str:
        excluded = FIELD_REPLACES.get(view_name.replace("form_","fields_").upper(),{}).get("exclude",[])
        content = []
        for field_data in self.__metadata:
            field_name = field_data["field_name"]
            if field_name in excluded:
                continue
            strinput = self.__input.get_html_replaced(view_name, field_name)
            content.append(strinput)

        return "".join(content)

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

    def get_list_tags_replaces(self) -> dict:
        replaces = {
            "FIELDS_QUERY_LIST": self.__get_query_list_and_entity(FIELD_REPLACES["FIELDS_QUERY_LIST"]["exclude"]),
            "FIELDS_QUERY_ENTITY": self.__get_query_list_and_entity(FIELD_REPLACES["FIELDS_QUERY_ENTITY"]["exclude"]),
            "FIELDS_GRID_HEADERS": self.__get_grid_headers(FIELD_REPLACES["FIELDS_GRID_HEADERS"]["exclude"]),
            "FIELDS_FILTERCONF": self.__get_filterconf(FIELD_REPLACES["FIELDS_FILTERCONF"]["exclude"]),
        }

        return replaces
