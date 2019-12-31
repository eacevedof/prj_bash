#!/bin/sh

# debe lanzar docker-compose up desde cualquier ruta
# algo como: dockerc.sh <proyecto>/xxxx/
# haria un cd y ejecutaria docker-compose up
# podria hacer dockerc.sh docker_imgs/symf01 y levantaria esos contenedores

# dockerc.sh <proyecto>

declare -A dcompose
rootpath="/e/projects"
dcompose[symf01]="$rootpath/prj_docker_imgs/"
dcompose[symf02]="$rootpath/prj_docker_imgs/"
dcompose[xnmp]="$rootpath/prj_docker_imgs/"
dcompose[xnp]="$rootpath/prj_docker_imgs/"

#capturo el <proyecto>
arg1=$1
# echo "arg1:$arg1"

if [[ $arg1 == "." ]]; then 
  fullpath=$PWD
  # echo "fullpath $fullpath"
fi

# si ese arg es una clave y tiene un valor
if [[ ! -z ${dcompose[$arg1]} ]]; then
  fullpath=${dcompose[$arg1]}$arg1
fi

if [[ ! -d $fullpath ]]; then 
  echo "not dir: $arg1"
  exit 1
fi

echo "fullpath ok:$fullpath"

# si todo ha ido bien compruebo que exista docker-compose.yml
ymlpath=$fullpath
ymlpath+="/docker-compose.yml"
echo "ymlpath: $ymlpath"

if [[ ! -f $ymlpath ]]; then
  echo "no docker-compose.yml"
  exit 1
fi

echo "cd fullpath"
cd $fullpath
echo "ejecuto docker-compose up"
docker-compose up
exec bash


