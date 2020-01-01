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

#capturo el <proyecto> | <stop:1>
prjkey=$1
stop=$2
# echo "prjkey:$prjkey"

if [[ $prjkey == "." ]]; then 
  fullpath=$PWD
  # echo "fullpath $fullpath"
fi

# si ese arg es una clave y tiene un valor
if [[ ! -z ${dcompose[$prjkey]} ]]; then
  fullpath=${dcompose[$prjkey]}$prjkey
fi

if [[ ! -d $fullpath ]]; then 
  echo "not dir: $prjkey"
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

# nueva ventana bash
start E:\\programas\\x64\\git\\git-bash.exe --cd="$fullpath"

echo "cd fullpath"
cd $fullpath

if [[ ! -z "$stop" ]]; then
  echo "docker-compose stop"
  docker-compose stop
  docker-compose ps
  docker-compose images
  exit
fi

echo "docker-compose up"
docker-compose ps
docker-compose up

