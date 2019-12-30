#!/bin/sh

##
# abre un directorio dentro de visualstudio code
#

#capturo el primer argumento
arg1=$1

#formo el nombre del proyecto
prjfolder="prj_$arg1"
fullpath="/e/projects/$prjfolder"
# si no hay argumento (nombre del proyecto)
if [[ -z "$arg1" ]] || [[ $arg1="." ]]; then
  # abro donde estoy
  fullpath=$PWD
fi

if [[ ! -d $fullpath ]]; then 
  echo "not dir: $fullpath"
  exit 1
fi

code $fullpath
