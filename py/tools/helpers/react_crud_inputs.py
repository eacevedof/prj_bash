from typing import List

FIELD_REPLACES = {
    "FIELDS_CLONE": {
        """
        <div className="col-12">
          <label htmlFor="txt-%field_name%" className="form-label">%label-description%</label>
          <input type="text" className="form-control" id="txt-%field_name%"
            
            value={formdata.%field_name%}
            disabled 
          />
        </div>
        """
    },
    "FIELDS_DELETE": {
        "exclude": [
            "processflag",
            "insert_platform", "insert_user", "insert_date",
            "update_platform", "update_user", "update_date",
            "delete_platform", "delete_user", "delete_date",
            "cru_csvnote", "is_erpsent", "is_enabled",
            "i", "code_cache",
            "id", "id_user",
        ],
    },
    "FIELDS_DELETELOGIC": {
        "exclude": [
            "processflag",
            "insert_platform", "insert_user", "insert_date",
            "update_platform", "update_user", "update_date",
            "delete_platform", "delete_user", "delete_date",
            "cru_csvnote", "is_erpsent", "is_enabled",
            "i", "code_cache",
            "id", "id_user",
        ],
    },
    "FIELDS_DETAIL": {
        "exclude": [
            "processflag",
            "insert_platform", "insert_user", "insert_date",
            "update_platform", "update_user", "update_date",
            "delete_platform", "delete_user", "delete_date",
            "cru_csvnote", "is_erpsent", "is_enabled",
            "i",
            "id", "id_user",
        ],
    },
    "FIELDS_INSERT": {
        "exclude": [
            "processflag",
            "insert_platform", "insert_user", "insert_date",
            "update_platform", "update_user", "update_date",
            "delete_platform", "delete_user", "delete_date",
            "cru_csvnote", "is_erpsent", "is_enabled",
            "i", "code_cache",
            "id", "id_user",
        ],
        "defaults": {}
    },
    "FIELDS_UPDATE": {
        "exclude": [
            "processflag",
            "insert_platform", "insert_user", "insert_date",
            "update_platform", "update_user", "update_date",
            "delete_platform", "delete_user", "delete_date",
            "cru_csvnote", "is_erpsent", "is_enabled",
            "i", "code_cache",
            "id", "id_user"
        ],
    },
    "FIELDS_QUERY_LIST": {
        "exclude": [
            "processflag",
            "insert_platform", "insert_user",  # "insert_date",
            "update_platform", "update_user",  # "update_date",
            "delete_platform", "delete_user",  # "delete_date",
            "cru_csvnote", "is_erpsent",  # "is_enabled",
            "i",
            "id", "code_cache",
        ],
    },

    "FIELDS_GRID_HEADERS": {
        # { text: 'Code', value: 'code_erp' },
        "exclude": [
            "processflag",
            "insert_platform", "insert_user", "insert_date",
            "update_platform", "update_user", "update_date",
            "delete_platform", "delete_user",  "delete_date",
            "cru_csvnote", "is_erpsent", "is_enabled",
            "i",
            "id", "code_cache",
        ],
    },

    "FIELDS_FILTERCONF": {
        # {name: "id", labels:["n","n","id"]},
        "exclude": [
            "processflag",
            "insert_platform", "insert_user", "insert_date",
            "update_platform", "update_user", "update_date",
            "delete_platform", "delete_user",  "delete_date",
            "cru_csvnote", "is_erpsent", "is_enabled",
            "i",
            "id", "code_cache",
        ],
    }

}

class ReactCrudFields:

    def __init__(self, metadada):
        self.__metadata = metadada
        self.__load_defvalues_by_type()

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

    def __load_defvalues_by_type(self):
        self.__default_values = {
            "int": 0,
            "decimal": 0.00,
            "varchar": "\"\"",
            "datetime": "\"\"",
            "timestamp": "\"\"",
        }

    def __get_field_and_length(self, tag_name: str) -> List:
        fields = []
        for field_data in self.__metadata:
            field_name = field_data.get("field_name", "")
            if self.__in_excluded_by_tag(tag_name, field_name):
                continue

            field_length = self.__get_field_length(field_data)
            field_type = field_data.get("field_type", "")
            default_value = self.__default_values[field_type]

            comment = f"//{field_type}({field_length})" if field_length else f"//{field_type}"
            txt = f"{field_name}: {default_value}, {comment}"
            fields.append(txt)
        return fields

    def __in_excluded_by_tag(self, tag_name: str, field_name: str) -> bool:
        return field_name in FIELD_REPLACES[tag_name]["exclude"]

    def get(self, tag_name: str) -> str:
        fields = self.__get_field_and_length(tag_name)
        return "\n".join(fields)
