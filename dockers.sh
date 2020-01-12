#!/bin/sh

# dockers.sh <cont-NAMES>|<CONTAINER ID> <open new win bash>
containerid=$1
iswinbash=$2

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

