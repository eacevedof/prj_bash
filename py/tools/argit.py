import sys
from inspect import signature
from pprint import pprint

def get_nargs():
    return len(sys.argv)

def getarg(ipos=0):
    if ipos < len(sys.argv):
        return sys.argv[ipos]
    return ""

def get_nfuncparams(fnobject):
    objsig = signature(fnobject)
    objparams = objsig.parameters
    # pprint(objparams)
    #die("get_numparams")
    return len(objparams)

def get_modulename():
    modulefunc = getarg(1)
    armodfunc = [s.strip() for s in modulefunc.split(".")]
    return armodfunc[0]

def get_funcname():
    modulefunc = getarg(1)
    armodfunc = [s.strip() for s in modulefunc.split(".")]
    strfuncname = armodfunc[1] if len(armodfunc)>1 else "index"
    return strfuncname

def showhelp():
    from help import index
    index()
