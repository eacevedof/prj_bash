#!/usr/bin/python

import sys
from importlib import import_module
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

if modulefunc=="--help" or modulefunc=="-help":
    from help import index
    index()
    die("\n\t--- END HELP ---")
    # die(f"Wrong argument 1 passed: {modulefunc} must be: <module>.<function>")

armodfunc = [s.strip() for s in modulefunc.split(".")]

module = armodfunc[0]
function = armodfunc[1] if len(armodfunc)>1 else "index"

def run():
    #importlib.import_module("routines",f"{module}.*")
    # importlib.import_module(".routines",f"{module}.*")
    # importlib.import_module(f"routines.{module}")
    imodule = import_module(f"routines.{module}")
    func = getattr(imodule,function)
    func(strparam)
    die(f" -- END --")

run()
