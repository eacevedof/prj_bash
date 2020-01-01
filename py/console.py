#!/usr/bin/python

import sys
from pprint import pprint
from routines.udemy import *

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

def getarg(ipos=0):
    return sys.argv[ipos]

argument = getarg(1)
module = getarg(2)
funcname = getarg(3)

if module=="udemy":
    if funcname=="index":
        index()
    else:
        pprint("no func found")
        pprint(funcname)
else:
    pprint("no module found")
    print(module)
