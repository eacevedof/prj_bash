#!/bin/sh

# dockers.sh <cont-NAMES>|<CONTAINER ID> <open new win bash>
paththis=$PWD

containerid=$1
iswinbash=$2


# compruebo si existe el comando de windows start
if [ -x "$(command -v start)" ]; then
  # nueva ventana bash
  start E:\\programas\\x64\\git\\git-bash.exe --cd="$fullpath"
else
  open -a Terminal $fullpath
fi

if [[ ! -z "$iswinbash" ]]; then
  # start E:\\programas\\x64\\git\\git-bash.exe --cd="$PWD" --login -i -c "docker ps"
  # start "E:\\programas\\x64\\git\\git-bash.exe" --cd="$PWD" --login -i -c "docker ps; read"
  # start E:\\programas\\x64\\git\\git-bash.exe --login -i -c "docker ps" --cd="$PWD" 
  start E:\\programas\\x64\\git\\git-bash.exe --cd="$PWD" 
  # start E:\\programas\\x64\\git\\git-bash.exe --cd="$PWD" --login -i
  # start E:\\programas\\x64\\git\\git-bash.exe --cd="$PWD" -c docker ps 
fi

if [[ ! -z "$containerid" ]]; then
  winpty docker exec -it $containerid bash
  # echo "hola"
fi

