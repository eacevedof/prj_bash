# routines.marketingmodel.py
print("routines.marketingmodel.py")
import traceback
import requests
from py.tools.tools import pr, pd
from py.services.marketing_crud.marketing_crud_service import MarketingCrud
from py.components.component_mysql import ComponentMysql
from py.components.component_crud import ComponentCrud

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
        "server": "localhost",
        "user": "root",
        "password": "1234",
        "database": "db_anytest",
        #"port": 3307
    })

    crud = ComponentCrud()
    sql = crud.set_comment("test insert")\
            .set_table("app_array")\
            .add_insert_fv("type","xxx")\
            .add_insert_fv("description","Dsc Xxxx")\
            .add_insert_fv("order_by",100)\
            .get_insert()
    crud = ComponentCrud()
    sql = crud\
            .set_comment("test update")\
            .set_table("app_array")\
            .add_update_fv("type","yyyy")\
            .add_update_fv("description","holas")\
            .add_update_fv("order_by",22)\
            .add_update_fv("code_erp", None)\
            .add_and("id=293")\
            .get_update()


    db.exec(sql)

    crud = ComponentCrud()
    sql = crud.set_table("base_user as m")\
            .set_comment("hola mundo")\
            .set_getfields(["count(m.id) as n_by_lang","ar1.description as language"])\
            .add_join("LEFT JOIN app_array ar1 ON m.id_language = ar1.id AND ar1.type='language'")\
            .add_and("m.id > 10")\
            .add_and("m.id < 300") \
            .add_groupby("ar1.description")\
            .add_having("count(m.id)>62")\
            .add_orderby("ar1.description","DESC")\
            .set_limit(500)\
            .get_select_from()
    result = db.query(sql)
    pr(db.get_errors())
    pr(result)


    sql = "update base_user set fullname='señor juan' where id=360"
    db.exec(sql)
    result = db.query("select id, fullname from base_user where id=360")
    pr(result)
    db.close()

    if db.is_error():
        pr(db.get_errors())
        pass

    pd("fin")
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
