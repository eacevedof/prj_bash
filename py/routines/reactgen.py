# routines.image.py
# py.sh reactgen <dbname> <table>

from tools.tools import is_dir, scandir, get_now, pr, mkdir, get_basename
import shutil
import os

# conectar con la bd

def index(db, table):
    pr(db,"db")
    pr(table,"table")

