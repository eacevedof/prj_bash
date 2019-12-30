#!/bin/sh
declare -a projects=(
    "prj_docker" "prj_docker_ci" "prj_docker_imgs" "prj_doctrine2" "prj_elchalanaruba" 
    "prj_flutter" "prj_js" "prj_jsonup" "prj_jswebpack" "prj_linux" "prj_mysqlhive" "prj_phptests" 
    "prj_platziphp" "prj_python37" "prj_reactjs3" "prj_symfony" "prj_theframework" 
    "prj_theframework_helpers" "prj_wordpress"
    )

for i in "${projects[@]}"
do
    echo $i
done
