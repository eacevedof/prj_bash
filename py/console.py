#!/usr/bin/python

import sys
from importlib import import_module
from tools.argit import *

def die(strmsg):
    print(f"console.py: {strmsg}")
    sys.exit()

modulename = get_modulename()
if modulename=="--help" or modulename=="-help" or modulename=="-h":
    showhelp()
    sys.exit()

def run():
    if get_nargs() < 2:
        die("\n\tWrong request!!. \n\tError: Missing arguments!. \n\tTry: \n\t  py.sh -h to check manual")

    #importlib.import_module("routines",f"{module}.*") nok
    # importlib.import_module(".routines",f"{module}.*") nok
    # importlib.import_module(f"routines.{module}") nok
    try:
        #print("argv"); pprint(sys.argv); die("-- end argv--")
        imodule = import_module(f"routines.{modulename}")
        funcname = get_funcname()
        objfunc = getattr(imodule, funcname)
        ifnparams = get_nfuncparams(objfunc)
        # print(ifnparams)
        # die(ifnparams)
        params = []
        if ifnparams>0:
            for iposition in range(1, ifnparams+1):
                argval = getarg(iposition + 1)
                print(f"argval:{argval} for {iposition}")
                if argval!="":
                    params.append(argval)

        # pprint(params); die("params to pass")
        objfunc(*params)

    except Exception as error:
        die(f" error: {error}")

run()
