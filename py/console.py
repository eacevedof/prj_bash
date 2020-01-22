#!/usr/bin/python

import sys
from pprint import pprint

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

def getarg(ipos=0):
    return sys.argv[ipos]

argument = getarg(1)
funcname = getarg(2)
module = getarg(3)

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
else:
    pprint("no module found")
    print(module)
