PATH_MODULE = "/Users/ioedu/projects/prj_eafpos/frontend/restrict/src/modules"
FOLDER_TEMPLATE = "zzz-tpl"

MODEL_REPLACES = {
    "zzz-tpls": "app-tables",
    "zzz-tpl": "app-table",
    "zzz_tpls": "app_tables",
    "zzz_tpl": "app_table",
    "ZzzTpls": "AppTables",
    "ZzzTpl": "AppTable",
    "Tpls": "Tables",
    "Tpl": "Table",
    "tpls": "tables",
    "tpl": "table"
}

FORM_REPLACES = {
    "FORM_CLONE": {
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
    "FORM_DELETE": {
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
    "FORM_DELETELOGIC": {
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
    "FORM_DETAIL": {
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
    "FORM_INSERT": {
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
    "FORM_UPDATE": {
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

    "FORM_QUERY_ENTITY": {
        "exclude": [
            "processflag",
            "insert_platform", "insert_user",  # "insert_date",
            "update_platform", "update_user",  # "update_date",
            "delete_platform", "delete_user",  # "delete_date",
            "cru_csvnote", "is_erpsent",  # "is_enabled",
            "i",
            "code_cache",
        ],
    }
}

FIELD_REPLACES = {
    "FIELDS_CLONE": {
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
        ],
    },

    "FIELDS_QUERY_ENTITY": {
        "exclude": [
            "processflag",
            "insert_platform", "insert_user",  # "insert_date",
            "update_platform", "update_user",  # "update_date",
            "delete_platform", "delete_user",  # "delete_date",
            "cru_csvnote", "is_erpsent",  # "is_enabled",
            "i",
            "code_cache",
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

INPUTS_TPLS = {
    "FORM_CLONE":{
        "html": """
            <div className="col-12">
              <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
              <input type="text" className="form-control" id="txt-%field_name%"
                
                value={formdata.%field_name%}
                disabled 
              />
            </div>
        """,
    },

    "FORM_DELETE":{
        "html": """
            <div className="col-12">
              <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
              <input type="text" className="form-control" id="txt-%field_name%" placeholder="placeholder-%field_name%" 
                
                value={formdata.%field_name%}
                disabled 
              />
            </div>
        """
    },

    "FORM_DELETELOGIC":{
        "html": """
            <div className="col-12">
              <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
              <input type="text" className="form-control" id="txt-%field_name%" placeholder="placeholder-%field_name%" 
                
                value={formdata.%field_name%}
                disabled 
              />
            </div>
        """
    },

    "FORM_DETAIL":{
        "html": """
          <div className="row">
            <div className="col-6">label-%field_name%</div>
            <div className="col-6">{formdata.%field_name%}</div>
          </div>
        """
    },

    "FORM_INSERT":{
        "html": """
          <div className="col-12">
            <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
            <input type="text" className="form-control" id="txt-%field_name%" placeholder="placeholder-%field_name%"
              value={formdata.%field_name%}
              onChange={updateform}
            />
          </div> 
        """
    },

    "FORM_UPDATE":{
        "html": """
          <div className="col-12">
            <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
            <input type="text" className="form-control" id="txt-%field_name%" placeholder="placeholder-%field_name%"
              value={formdata.%field_name%}
              onChange={updateform}
            />
          </div> 
        """
    },
}

DEFAULT_VALUES_TYPES = {
    "int": 0,
    "tinyint": 0,
    "decimal": 0.00,
    "varchar": "\"\"",
    "datetime": "\"\"",
    "timestamp": "\"\"",
}
