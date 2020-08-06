#!/bin/sh

# py.sh <path-to-function-in-package routines <arg1> ... <arg5>
# ejemplo:
#   py.sh udemy.index "C:\Users\ioedu\Desktop\temp.php"

# el dir de este script (py.sh)
thisdir=$(dirname "$0")
. "$thisdir/utils.sh"


# ruta a mi gestor de consola de python
pypath=$thisdir"/py/console.py"

args=("$@")

clear
# echo ${arg[0]}    #console.py
# echo ${arg[1]}    #module.action in package routines
# echo ${arg[2...]} #anyparam
py $pypath ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]}
