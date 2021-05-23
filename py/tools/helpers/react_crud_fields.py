from typing import List

FIELD_REPLACES = {
    "FIELDS_CLONE": {
        "exclude": [],
        "defaults": {}
    },
    "FIELDS_DELETE": {
        "exclude": [],
        "defaults": {}
    },
    "FIELDS_DELETELOGIC": {
        "exclude": [],
        "defaults": {}
    },
    "FIELDS_DETAIL": {
        "exclude": [],
        "defaults": {}
    },
    "FIELDS_INSERT": {
        "exclude": [],
        "defaults": {}
    },
    "FIELDS_UPDATE": {
        "exclude": [],
        "defaults": {}
    },
}

class ReactCrudFields:

    def __init__(self, metadada):
        self.__metadata = metadada

    def __get_field_length(self, field_data: dict) -> str:
        field_length = field_data.get("field_length","")
        if not field_length:
            integers = field_data.get("ntot","")
            if not integers:
                return ""
            decimals = field_data.get("ndec","")
            integers = str(integers)
            decimals = str(decimals)
            field_length = integers + "," + decimals

        return field_length

    def __get_field_and_length(self, tag_name: str) -> List:
        fields = []
        for field_data in self.__metadata:
            field_name = field_data.get("field_name","")
            if self.__in_excluded_by_tag(tag_name, field_name):
                continue

            field_length = self.__get_field_length(field_data)
            field_type = field_data.get("field_type","")
            comment = f"//{field_type}({field_length})" if field_length else f"//{field_type}"
            txt = f"{field_name}: \"\", {comment}"
            fields.append(txt)
        return fields

    def __in_excluded_by_tag(self, tag_name: str, field_name: str) -> bool:
        return field_name in FIELD_REPLACES[tag_name]["exclude"]

    def get(self, tag_name: str) -> str:
        fields = self.__get_field_and_length(tag_name)
        return "\n".join(fields)
