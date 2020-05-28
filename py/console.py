#!/usr/bin/python

import sys
import importlib
from pprint import pprint

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

def die(strmsg):
    print(f"console.py: {strmsg}")
    sys.exit()

def getarg(ipos=0):
    if ipos < len(sys.argv):
        return sys.argv[ipos]
    return ""

#arg1: módulo.funcion arguments
#arg2: paarameters
modulefunc = getarg(1)
strparam = getarg(2)

if modulefunc=="":
    die("No argument 1 (module.func) is empty")

armodfunc = [s.strip() for s in modulefunc.split(".")]
if len(armodfunc) != 2:
    die(f"Wrong argument 1 passed: {modulefunc} must be: <module>.<function>")

module = armodfunc[0]
function = armodfunc[1]

def run():
    eval(f"from routines.{module} import *")
    eval(f"{function}('{strparam}')")
    die(f" -- END --")

run()

if module=="udemy":
    from routines.udemy import *
    if funcname=="index":
        index(argument)
    else:
        pprint("no func found")
        pprint(funcname)
elif module=="dump":
    from routines.dump import *
    if funcname=="index":
        index(argument)
    else:
        pprint("no func found")
        pprint(funcname)
elif module=="react":
    from routines.react import *
    if funcname=="index":
        index(argument)
    else:
        pprint("no func found")
        pprint(funcname)   

elif module=="deploy":
    from routines.deploy import *
    if funcname=="index":
        index(argument)
    else:
        eval(f"{funcname}('{argument}')")
        #pprint("no func found")
        pprint(funcname)
else:
    pprint("console.py: no module found")
    print(module)
