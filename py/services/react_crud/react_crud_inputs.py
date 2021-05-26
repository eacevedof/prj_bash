from typing import List
from py.services.react_crud.react_crud_config import INPUTS_TPLS

class ReactCrudInputs:

    def __init__(self):
        pass

    def get_html_replaced(self, view_name: str, field_name: str) -> str:
        upper = view_name.upper()
        html = INPUTS_TPLS.get(upper, {}).get("html","")
        return html.replace("%field_name%", field_name)
