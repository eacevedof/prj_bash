#!/bin/sh

##
# abre un directorio dentro de visualstudio code
#

#capturo el primer argumento
arg1=$1
# echo "arg1: $arg1"

# import utils.hs
. "$thisdir/utils.sh"



#formo el nombre del proyecto
prjfolder="prj_$arg1"
fullpath="/e/projects/$prjfolder"
# echo $fullpath

# si no hay argumento (nombre del proyecto) o si el argumento es . renombro fullpath
if [ -z "$arg1" ] || [[ $arg1 == "." ]]; then
  # echo "cambio a dir actual: arg=$arg1"
  # abro donde estoy
  fullpath=$PWD
fi

if [[ ! -d $fullpath ]]; then 
  echo "not dir: $fullpath"
  exit 1
fi

echo "opening vscode with $fullpath"
code $fullpath
