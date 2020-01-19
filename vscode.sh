#!/bin/sh

##
# abre un directorio dentro de visualstudio code
#

#capturo el primer argumento
arg1=$1
# echo "arg1: $arg1"

# import utils.hs
thisdir=$(dirname "$0")
. "$thisdir/utils.sh"


if [[ $1 == "-h" ]]
then
  echo "search (in projects/prj_ path to open folder in vs code "
  echo "\nTry:\n vscode.sh <sufix in projects/prj_folder>"
  echo "examples:\n vscode.sh python37"
  echo " vscode.sh reactjs3"
  exit 0
fi


#formo el nombre del proyecto
prjfolder="prj_$arg1"
fullpath="/e/projects/$prjfolder"
if is_ios; then
  fullpath=$PATHPRJ"/$prjfolder"
fi

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
if is_win; then
  code $fullpath
fi
if is_ios; then 
  # abrit visual stoudio code en mac
  open -a /Applications/Visual\ Studio\ Code.app $fullpath
  # code $fullpath # no va!!
fi

