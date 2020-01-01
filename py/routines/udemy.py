# routines.udemy.py

def file_get_contents(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        return f"no file found: {filename}"

def index(pathfile):
    #print("routines.index")
    fc = file_get_contents(pathfile)
    print(fc)
