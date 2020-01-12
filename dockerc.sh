#!/bin/sh

# debe lanzar docker-compose up desde cualquier ruta
# algo como: dockerc.sh <proyecto>/xxxx/
# haria un cd y ejecutaria docker-compose up
# podria hacer dockerc.sh docker_imgs/symf01 y levantaria esos contenedores

# dockerc.sh <proyecto>

# esta variable se exporta en .zshrc
# echo $PATHPRJ; exit

pathprj="/e/projects"
if [[ ! -z "${PATHPRJ}" ]]; then
  pathprj="$PATHPRJ"
fi

# array proyectos docker
# esto da error: 
#   line 19: declare: -A: invalid option
#   https://stackoverflow.com/questions/6047648/bash-4-associative-arrays-error-declare-a-invalid-option
# he tenido que instalar la ultima version de bash brew install bash
# en /etc/bash he agregado la ruta /usr/local/bin/bash se puede comprobar con: type bash
# declare -A images
declare images
pathimgs="$pathprj/prj_docker_imgs"

images[symf01]=$pathimgs
images[symf02]=$pathimgs
images[symf03]=$pathimgs
images[xnmp]=$pathimgs
images[xnp]=$pathimgs

#capturo el <proyecto> | <option:1>
imgkey=$1
option=$2
# echo "imgkey:$imgkey"; exit

if [ $imgkey == "-h" ]; 
then
  echo "\nTry:\n docker.sh <subfolder in prj_docker_imgs> | <ps|down|up> \n"
  # echo "subfolders of $pathimgs:";
  echo "subfolders:"
  for subpath in $(ls -d $pathimgs/*/);
  do
    #echo $subpath 
    strtemp=${subpath//"$pathimgs"/""}
    strtemp=${strtemp//\//""}
    # imprimo en negrita
    echo "\t\033[1m$strtemp\033[0m"
  done
  # ls -d "$pathprj/prj_docker_imgs/*"
  exit 0
fi

if [[ $imgkey == "." ]]; then 
  fullpath=$PWD
  # echo "fullpath $fullpath"
fi

# si ese arg es una clave y tiene un valor
if [[ ! -z ${images[$imgkey]} ]]; then
  fullpath="${images[$imgkey]}/$imgkey"
fi

if [[ ! -d $fullpath ]]; then 
  echo "not dir: $fullpath"
  exit 1
fi

echo "fullpath ok: $fullpath"

# si todo ha ido bien compruebo que exista docker-compose.yml
ymlpath=$fullpath
ymlpath+="/docker-compose.yml"
echo "ymlpath: $ymlpath"

if [[ ! -f $ymlpath ]]; then
  echo "no docker-compose.yml"
  exit 1
fi

# echo "cd fullpath"
cd $fullpath
clear

if [[ $option == "ps" ]]; then 
  # echo "option: ps"
  docker-compose ps
  docker-compose images
  exit
fi

# los echos son tratados como comandos
if [[ $option == "down" ]]; then 
  # echo "option: down"
  docker-compose down --rmi all
  docker-compose ps
  docker-compose images
  exit
fi

# compruebo si existe el comando de windows start
if [ -x "$(command -v start)" ]; then
  # nueva ventana bash
  start E:\\programas\\x64\\git\\git-bash.exe --cd="$fullpath"
else
  open -a Terminal $fullpath
fi

echo "option: up"
docker-compose ps
docker-compose up --build
