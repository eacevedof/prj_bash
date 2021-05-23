from typing import List

INPUTS_TPLS = {
    "FORM_CLONE":
        """
        <div className="col-12">
          <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
          <input type="text" className="form-control" id="txt-%field_name%"
            
            value={formdata.%field_name%}
            disabled 
          />
        </div>
        """,

    "FORM_DELETE":
        """
        <div className="col-12">
          <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
          <input type="text" className="form-control" id="txt-%field_name%"
            
            value={formdata.%field_name%}
            disabled 
          />
        </div>
        """,

    "FORM_DELETELOGIC":
        """
        <div className="col-12">
          <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
          <input type="text" className="form-control" id="txt-%field_name%"
            
            value={formdata.%field_name%}
            disabled 
          />
        </div>
        """,

    "FORM_DETAIL":
        """
        <div className="col-12">
          <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
          <input type="text" className="form-control" id="txt-%field_name%"
            
            value={formdata.%field_name%}
            disabled 
          />
        </div>
        """,

    "FORM_INSERT":
        """
        <div className="col-12">
          <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
          <input type="text" className="form-control" id="txt-%field_name%"
            
            value={formdata.%field_name%}
            disabled 
          />
        </div>
        """,

    "FORM_UPDATE":
        """
        <div className="col-12">
          <label htmlFor="txt-%field_name%" className="form-label">label-%field_name%</label>
          <input type="text" className="form-control" id="txt-%field_name%"
            
            value={formdata.%field_name%}
            disabled 
          />
        </div>
        """,
}

class ReactCrudInputs:

    def __init__(self):
        pass

    def get(self, view_name: str, field_name: str) -> str:
        upper = view_name.upper()
        content = INPUTS_TPLS.get(upper, "")
        return content.replace("%field_name%",field_name)
