from typing import List

class ReactCrudFields:

    def __init__(self, metadada):
        self.__metadata = metadada

    def __get_field_and_length(self) -> List:
        fields = []
        for field_data in self.__metadata:
            field_name = field_data.get("field_name","")
            field_length = field_data.get("field_length") \
                if field_data.get("field_length") else field_data.get("ntot","") + "," + field_data.get("ndec","")
            txt = f"\"{field_name}\":\"\" //({field_length})"
            fields.append(txt)
        return fields

    def get(self) -> str:
        fields = self.__get_field_and_length()
        return ""
