#!/bin/sh

##
# abre un directorio dentro de projects
#

#capturo el primer argumento
arg1=$1
#formo el nombre del proyecto
prjfolder="prj_$arg1"

fullpath="/e/projects/$prjfolder"
if [[ $arg1 == "." ]]; then 
  fullpath=$PWD
  # echo "fullpath $fullpath"
fi

# si no es un dir
if [[ ! -d $fullpath ]]; then 
    echo "not dir: $fullpath"
    exit 1
fi

cd $fullpath
# start sh --login
# start bash --login
start bash 

# E:\programas\x64\git\bin
# bash.exe
# git.exe
# sh.exe

# E:\programas\x64\git\git-bash.exe --cd="e:\projects"
# (cd /e/projects/prj_python37 && start sh --login) 