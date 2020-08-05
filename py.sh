#!/bin/sh

# py.sh <path-a-funcion> <arg1> ... <arg5>
# ejemplo:
#   py.sh "C:\Users\ioedu\Desktop\temp.php"

# el dir de este script (py.sh)
thisdir=$(dirname "$0")
. "$thisdir/utils.sh"


# ruta a mi gestor de consola de python
pypath=$thisdir"/py/console.py"

args=("$@")
# if [ -z "$1" ] || [[ $1 == "-h" ]] # tambien func
if [ is_empty $1 ] || [[ $1 == "-h" ]]
then
  echo "\nTry:\n py.sh <module=[in routines folder]>.<action=[any function index() by default]> <argument="">"
  echo "examples:\n py.sh udemy \"C:\Users\ioedu\Desktop\\\\temp.php\" #windows"
  echo " py.sh udemy \"/Users/ioedu/Desktop/temp.php\" #mac\n"
  exit 0
fi

#recupero parametros
argument=$([ -z "$1" ] && echo "" || echo "$1")  #module.action
# action=$([ -z "$2" ] && echo "index" || echo "$2")  #index
# module=$([ -z "$3" ] && echo "udemy" || echo "$3")
clear
# echo $pypath    #console.py
# echo $argument  #module.action
# echo $action    #index

# python3 $pypath $argument $action $module
#py $pypath $argument $action $module
py $pypath ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]}
