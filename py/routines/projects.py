from tools.tools import get_dicconfig
from pprint import pprint

def index():
    list_data = get_dicconfig().get_data()
    projects = []
    for dc in list_data:
        projects.append(dc.get("id",""))
    projects.sort()
    for i, project in enumerate(projects):
        print(f"({i}) {project}")

