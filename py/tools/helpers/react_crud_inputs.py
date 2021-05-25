from typing import List

# separar por tipos

INPUTS_TPLS = {
    //
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

class ReactCrudInputs:

    def __init__(self):
        pass

    def get_html_replaced(self, view_name: str, field_name: str) -> str:
        upper = view_name.upper()
        html = INPUTS_TPLS.get(upper, {}).get("html","")
        return html.replace("%field_name%", field_name)
