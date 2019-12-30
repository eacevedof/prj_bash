#!/bin/sh

# array de proyectos
declare -a projects=(
      "prj_docker" "prj_docker_ci" "prj_docker_imgs" "prj_doctrine2" "prj_elchalanaruba" 
      "prj_flutter" "prj_js" "prj_jsonup" "prj_jswebpack" "prj_linux" "prj_mysqlhive" "prj_phptests" 
      "prj_platziphp" "prj_python37" "prj_reactjs3" "prj_symfony" "prj_theframework" 
      "prj_theframework_helpers" "prj_wordpress" "prj_bash"
    )

#echo $1
input=$1
project="prj_$input"
#echo $project
#exit

if [[ " ${projects[@]} " =~ " ${project} " ]]; then
  #echo "executing cd"
  fullpath="/e/projects/$project"
  # echo $fullpath
  cd $fullpath
  exec bash
  # cd "$(dirname "${fullpath}")"
else
  echo "project not found in array"
fi
