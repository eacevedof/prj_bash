# routines.marketingmodel.py
print("routines.marketingmodel.py")
import traceback
import requests
from py.tools.tools import pr
from py.services.marketing_crud.marketing_crud_service import MarketingCrud
from py.components.component_mysql import ComponentMysql

BASE_URL = "http://localhost:900"
USER = "fulanito"
PASSWORD = "MaFaLDa1234"


def login() -> str:
    url = f"{BASE_URL}/apify/security/login"
    post = {"user": USER, "password": PASSWORD}
    req = requests.Session()
    req.headers.update({"origin": "http://localhost:3000"})
    r = req.post(url, data=post)
    dict = r.json()
    return dict.get("data", {}).get("token", "")


def get_metadada(tablename, token) -> dict:
    url = f"{BASE_URL}/apify/fields/c1/db-eafpos/{tablename}"
    post = {"apify-usertoken": token}

    req = requests.Session()
    req.headers.update({"origin": "http://localhost:3000"})
    r = req.post(url, data=post)
    dict = r.json()
    return dict.get("data", [])

def index(tablename):
    db = ComponentMysql(arconn={
        "server": "localhost:3307",
        "user": "root",
        "password": "root",
        "database": "db_marketing"
    })

    pass
    try:
        token = login()
        if token:
            metadata = get_metadada(tablename, token)
            if not metadata:
                pr(f"No metadata for {tablename}")
                return

            marketing_crud = MarketingCrud(tablename, metadata)
            marketing_crud.run()
        else:
            pr(f"No token found for {tablename}")
    except Exception as error:
        traceback.print_exc()
        pr(error)

if __name__ == "__main__":
    # esto no va. Da error en los imports ya que no encuentra el módulo py.
    login()
