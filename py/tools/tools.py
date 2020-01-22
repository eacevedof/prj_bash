# tools.tools.py
import sys
# from pprint import pprint

def printx(mxvar):

    if isinstance(mxvar,list):
        for i, item in enumerate(mxvar):
            print(i," => ",item)
    else:
        print(mxvar)

def pr(var,title=""):
    if title!="":
        print(title)
    printx(var)

def pd(var,title=""):
    if title!="":
        print(title)
    printx(var)
    sys.exit()

def file_get_contents(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        return f"no file found: {filename}"

def file_put_contents(filename,strdata=""):
    try:
        with open(filename, 'w') as f:
            f.write(strdata)
    except IOError:
        return f"no file found: {filename}"

def get_datetime():
    from datetime import datetime
    now = datetime.now()
    now.strftime("%Y-%m-%d %H:%M:%S")
    pr(now)
    now = str(now).replace("-","").replace(":","").replace(" ","")
    return now