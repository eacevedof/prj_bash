#!/bin/sh

# dockers.sh <cont-NAMES>|<CONTAINER ID> <open new win bash>
thisdir=$( dirname $0)

# import utils.hs
. "$thisdir/utils.sh"

if [ -z "$1" ] || [[ $1 == "-h" ]];
then
  echo "> opens bash session in container"
  echo "> Try:\n dockers.sh <cont-NAMES>|<CONTAINER ID> <isnewwin any value>\n"
  echo "> example:  dockers.sh miubu 1"
  echo ""
  docker ps
  echo ""
  exit 0
fi

containerid=$1
newwindow=$2

# compruebo si existe el comando de windows start
if is_win; then
  if ! is_empty $newwindow; then 
    # start E:\\programas\\x64\\git\\git-bash.exe --cd="$PWD" --login -i -c "docker ps"
    # start "E:\\programas\\x64\\git\\git-bash.exe" --cd="$PWD" --login -i -c "docker ps; read"
    # start E:\\programas\\x64\\git\\git-bash.exe --login -i -c "docker ps" --cd="$PWD" 
    start E:\\programas\\x64\\git\\git-bash.exe --cd="$PWD" 
    # start E:\\programas\\x64\\git\\git-bash.exe --cd="$PWD" --login -i
    # start E:\\programas\\x64\\git\\git-bash.exe --cd="$PWD" -c docker ps 
  fi
  winpty docker exec -it $containerid bash
  exit 0
else
  if ! is_empty $newwindow; then 
    # osascript -e 'tell application "Terminal" to do script "echo hello"'
    # open -a Terminal $PWD; 
    # osascript -e 'tell application "Terminal" to do script "cd /Users/ioedu/"';
    # osascript -e `tell application "Terminal" to do script "cd $PWD"`;
    # osascript -e 'tell application "Terminal" to do script "cd' $PWD'"';
    # osascript -e "tell application \"Terminal\" to do script \"cd '$PWD/prj_bash'\""  ok
    osascript -e "tell application \"Terminal\" to do script \"cd '$PWD'\""
    # osascript <<END 
    #   tell application "Terminal"
    #     do script "cd \"`pwd`\";$1;exit"
    #   end tell
    # END;
  fi
  # docker exec --user="root" -it <container_name> /bin/bash
  docker exec --user="root" -it $containerid bash
  exit 0
fi

