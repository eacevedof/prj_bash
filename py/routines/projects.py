from tools.tools import get_dicconfig
from pprint import pprint

def index():
    list_data = get_dicconfig().get_data()
    projects = []
    for dc in list_data:
        projects.append({
            "id": dc.get("id", ""),
            "options": [k for k in dc.keys() if k!="id"].sort()
        })
    projects.sort()

    for i, dc in enumerate(projects):
        id = dc.get("id","")
        print(f"({i}) {id}")
        for j, opt in dc.get("options",[]):
            print(f"  - ({j}) {opt}")

