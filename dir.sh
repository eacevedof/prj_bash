#!/bin/sh

# dir.sh <project> 

project=$1

# creo una ruta por defecto
fullpath="/e/projects/prj_$project"

if [[ -z "$project" ]] || [[ ! -d $fullpath ]]; then
  fullpath=$PWD
fi

start $fullpath
