from typing import List

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
              <label htmlFor="txt-description" className="form-label">Description</label>
              <input type="text" className="form-control" id="txt-description" placeholder="Name of table" 
                
                value={formdata.description}
                disabled 
              />
            </div>
        """
    },

    "FORM_DELETELOGIC":{
        "html": """
            <div className="col-12">
              <label htmlFor="txt-description" className="form-label">Description</label>
              <input type="text" className="form-control" id="txt-description" placeholder="Name of table" 
                
                value={formdata.description}
                disabled 
              />
            </div>
        """
    },

    "FORM_DETAIL":{},

    "FORM_INSERT":{},

    "FORM_UPDATE":{},
}

class ReactCrudInputs:

    def __init__(self):
        pass

    def get_html_replaced(self, view_name: str, field_name: str) -> str:
        upper = view_name.upper()
        html = INPUTS_TPLS.get(upper, {}).get("html","")
        return html.replace("%field_name%", field_name)
