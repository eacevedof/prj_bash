#!/bin/sh

#capturo el primer argumento
arg1=$1
#formo el nombre del proyecto
prjfolder="prj_$arg1"
fullpath="/e/projects/$prjfolder"

# si es directorio
if [[ -d $fullpath ]]; then
  # cambia de directorio en la misma ventana
  cd $fullpath
  exec bash
else
  echo "folder: $fullpath not found"
fi