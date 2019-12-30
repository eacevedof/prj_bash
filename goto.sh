#!/bin/sh

#capturo el primer argumento
arg1=$1
#formo el nombre del proyecto
prjfolder="prj_$arg1"
fullpath="/e/projects/$prjfolder"

# si es directorio
if [[ -d $fullpath ]]; then 
  cd $fullpath
  exec bash
else
  echo "prjfolder $fullpath not found in array"
fi