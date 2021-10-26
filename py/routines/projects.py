from tools.tools import get_dicconfig
from pprint import pprint

def index():
    list_data = get_dicconfig().get_data()
    projects = []
    for dc in list_data:
        keys = list(dc.keys())
        keys = [k for k in keys if "id" not in k]
        keys.sort()

        projects.append({
            "id": dc.get("id", ""),
            "options": keys
        })


    for i, dc in enumerate(projects):
        id = dc.get("id","")
        print(f"({i}) {id}")
        options = dc.get("options",[])
        for j, opt in enumerate(options):
            print(f"  - [{j}] {opt}")

