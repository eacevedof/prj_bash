from typing import List

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

    def __get_field_and_length(self) -> List:
        fields = []
        for field_data in self.__metadata:
            field_name = field_data.get("field_name","")
            field_length = self.__get_field_length(field_data)
            field_type = field_data.get("field_type","")
            comment = f"//({field_length})" if field_length else f"//{field_type}"
            txt = f"\"{field_name}\":\"\" {comment}"
            fields.append(txt)
        return fields

    def get(self) -> str:
        fields = self.__get_field_and_length()
        return ""
