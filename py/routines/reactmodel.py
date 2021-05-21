# routines.reactmodel.py
print("routines.reactmodel.py")
from tools.tools import file_get_contents,pr,pd,file_put_contents,is_dir
import requests

BASE_URL = "http://localhost:900"
USER = "fulanito"
PASSWORD = "MaFaLDa1234"


def login() -> str:
    url = f"{BASE_URL}/apify/security/login"
    post = {"user":USER,"password":PASSWORD}
    req = requests.Session()
    req.headers.update({"origin":"http://localhost:3000"})
    r = req.post(url, data=post)
    dict = r.json()
    return dict.get("data",{}).get("token","")

def get_metadada(tablename, token) -> dict:
    url = f"{BASE_URL}/apify/fields/c1/db-eafpos/{tablename}"
    post = {"apify-usertoken":token}

    req = requests.Session()
    req.headers.update({"origin":"http://localhost:3000"})
    r = req.post(url, data=post)
    dict = r.json()
    return dict.get("data",[])


def index(tablename):
    pr(tablename)
    token = login()
    if token:
        metadata = get_metadada(tablename, token)

        pr(metadata)


