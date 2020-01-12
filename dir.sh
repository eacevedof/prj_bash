#!/bin/sh

# dir.sh <project> 

# esta variable se exporta en .zshrc
# echo $PATHPRJ; exit

pathprj="/e/projects"
if [[ ! -z "${PATHPRJ}" ]]; then
  pathprj="$PATHPRJ"
fi

project=$1
if [[ -z "$project" ]]; then
  echo " > Project must exist in $pathprj"
  echo " > No project passed. Try:\n dir.sh <project without prj_ prefix>"
  exit 1
fi

# creo una ruta por defecto
fullpath="$pathprj/prj_$project"
# echo $fullpath; exit
if [[ ! -d $fullpath ]]; then
  fullpath=$PWD
fi

# compruebo si existe el comando de windows start
if [ -x "$(command -v start)" ]; then
  start $fullpath
fi

# echo "fullpath: $fullpath"; #  exit
if [ -x "$(command -v open)" ]; then
  # https://stackoverflow.com/questions/11676007/how-do-you-open-a-new-mac-os-x-terminal-from-terminal-and-have-it-be-in-the-same
  # open -a Terminal $fullpath
  echo "opening: $fullpath"
  open $fullpath
fi

