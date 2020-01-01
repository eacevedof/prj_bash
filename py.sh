#!/bin/sh

# py.sh <modulo> <funcion> 

# el dir de este script (py.sh)
thisdir=$(dirname "$0")
# ruta a mi gestor de consola de python
pypath="$thisdir/py/console.py"

#recupero parametros
argument=$([ -z "$1" ] && echo "" || echo "$1")
module=$([ -z "$2" ] && echo "udemy" || echo "$2")
action=$([ -z "$3" ] && echo "index" || echo "$3")

py $pypath $argument $module $action