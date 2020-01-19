#!/bin/sh

# import utils.sh
thisdir=$(dirname "$0")
. "$thisdir/utils.sh"

#formo el nombre del proyecto
prjfolder="prj_$1"
fullpath="/e/projects/$prjfolder"
if is_ios; then fullpath=$PATHPRJ"/$prjfolder"; fi

# si es directorio
if [[ -d $fullpath ]]; then
  # cambia de directorio en la misma ventana
  cd $fullpath
  if is_win; then exec bash; fi
  if is_ios; then 
    # open -a Terminal $fullpath; abre pero no en ruta
    osascript -e "tell application \"Terminal\" to do script \"cd '$fullpath'\""
  fi
else
  echo "folder: $fullpath not found"
fi