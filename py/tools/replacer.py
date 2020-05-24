# como helper en ionos
# debe hacerse con Python 2.7.9
# ejemplo: 
#   python replacer.py "db_tinymarket" "dbs433055" /Users/ioedu/projects/prj_tinymarket-test/backend_web/db/db_tinymarket_20200522224117.sql
import sys

def file_get_contents(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        print("no file found:"+ filename)

def file_put_contents(filename,strdata=""):
    try:
        with open(filename, 'w') as f:
            f.write(strdata)
    except IOError:
        print("no file found:"+ filename)

def is_file(pathfile):
    from os import path
    return path.exists(pathfile)

def replace():
    args = sys.argv
    argslen = len(args)
    # busca esto, pon esto otro en archivo
    search = args[1] if 1 < argslen else ""
    #print("search: "+search)
    replace = args[2] if 2 < argslen else ""
    #print("replace: "+replace)
    pathtarget = args[3] if 2 < argslen else ""
    #print("pathtarget: "+pathtarget)

    print("search: "+search +", replace: "+replace +"pathtarget: "+pathtarget)

    if not is_file(pathtarget):
        print("file not found "+pathtarget)
        return

    content = file_get_contents(pathtarget)
    newcontent = content.replace(search,replace)
    file_put_contents(pathtarget,newcontent)
    print("replacing finished")

if __name__ == "__main__":
    replace()