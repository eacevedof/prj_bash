#!/bin/sh

##
# abre un directorio dentro de visualstudio code
#

#capturo el primer argumento
arg1=$1
#formo el nombre del proyecto
prjfolder="prj_$arg1"

fullpath="/e/projects/$prjfolder"
if [[ ! -d $fullpath ]]; then 
    echo "not dir: $fullpath"
    exit 1
fi

code $fullpath
