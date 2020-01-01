#!/bin/sh

# py.sh <argument=""> <action=index> <module=udemy>
# ejemplo:
#   py.sh "C:\Users\ioedu\Desktop\temp.php"

# el dir de este script (py.sh)
thisdir=$(dirname "$0")
# ruta a mi gestor de consola de python
pypath="$thisdir/py/console.py"

#recupero parametros
argument=$([ -z "$1" ] && echo "" || echo "$1")
action=$([ -z "$2" ] && echo "index" || echo "$2")
module=$([ -z "$3" ] && echo "udemy" || echo "$3")

clear
py $pypath $argument $action $module