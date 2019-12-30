#!/bin/sh

# array de proyectos
declare -a projects=(
      "prj_docker" "prj_docker_ci" "prj_docker_imgs" "prj_doctrine2" "prj_elchalanaruba" 
      "prj_flutter" "prj_js" "prj_jsonup" "prj_jswebpack" "prj_linux" "prj_mysqlhive" "prj_phptests" 
      "prj_platziphp" "prj_python37" "prj_reactjs3" "prj_symfony" "prj_theframework" 
      "prj_theframework_helpers" "prj_wordpress" "prj_bash"
    )

#capturo el primer argumento
arg1=$1
#formo el nombre del proyecto
prjfolder="prj_$arg1"

#compruebo si existe en el array
if [[ " ${projects[@]} " =~ " ${prjfolder} " ]]; then
  #ruta absoluta al proyecto
  fullpath="/e/projects/$prjfolder"
  #voy al directorio
  cd $fullpath
  #refresco el shell de lo contrario no se veria el cambio del directorio en la ventana donde estoy
  exec bash
else
  echo "prjfolder $arg1 not found in array"
fi
