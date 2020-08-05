#!/usr/bin/python

import sys
from importlib import import_module
from inspect import signature
from pprint import pprint

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

def die(strmsg):
    print(f"console.py: {strmsg}")
    sys.exit()

def get_nargs():
    return len(sys.argv)

def getarg(ipos=0):
    if ipos < len(sys.argv):
        return sys.argv[ipos]
    return ""

def get_numparams(fnobject):
    objsig = signature(fnobject)
    objparams = objsig.parameters
    # pprint(objparams)
    #die("get_numparams")
    return len(objparams)

#arg1: módulo.funcion arguments
#arg2: paarameters
modulefunc = getarg(1)
# iargs = len(sys.argv)
# objrange = range(2,iargs)

strparam2 = getarg(2)
strparam3 = getarg(3)
strparam4 = getarg(4)

if modulefunc=="--help" or modulefunc=="-help" or modulefunc=="-h":
    from help import index
    index()
    die("end help")
    # die(f"Wrong argument 1 passed: {modulefunc} must be: <module>.<function>")

armodfunc = [s.strip() for s in modulefunc.split(".")]
module = armodfunc[0]
strfuncname = armodfunc[1] if len(armodfunc)>1 else "index"

def run():
    if get_nargs() < 2:
        die("\n\tWrong request!!. \n\tError: Missing arguments!. \n\tTry: \n\t  py.sh -h to check manual")

    #importlib.import_module("routines",f"{module}.*") nok
    # importlib.import_module(".routines",f"{module}.*") nok
    # importlib.import_module(f"routines.{module}") nok
    try:
        print("argv"); pprint(sys.argv); die("-- end argv--")
        imodule = import_module(f"routines.{module}")
        func = getattr(imodule, strfuncname)
        iparams = get_numparams(func)
        # print(iparams)
        # die(iparams)
        params = []
        if iparams>0:
            for i in range(1,iparams+1):
                argval = getarg(i+1)
                # print(f"argval:{argval} for {i}")
                if argval!="":
                    params.append(argval)

        #pprint(params)
        #die("params to pass")
        func(*params)

    except Exception as error:
        die(f" error: {error}")

run()
