# routines.reactmodel.py
print("routines.reactmodel.py")
import requests
from py.tools.tools import pr
from py.tools.helpers.react_crud import ReactCrud

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
    token = login()
    if token:
        metadata = get_metadada(tablename, token)
        react_crud = ReactCrud(tablename, metadata)
        react_crud.run()
    pr("end reactmodel crud")
