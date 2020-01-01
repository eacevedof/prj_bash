#!/bin/sh

# py.sh <modulo> <funcion> 

# el dir de este script (py.sh)
thisdir=$(dirname "$0")
# ruta a mi gestor de consola de python
pypath="$thisdir/py/console.py"

#recupero parametros
module=$([ -z "$1" ] && echo "udemy" || echo "$1")
action=$([ -z "$2" ] && echo "index" || echo "$2")

py $pypath $module $action