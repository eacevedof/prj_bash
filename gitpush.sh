#!/bin/sh
# automatiza el push total de la carpeta donde estoy

# import utils.sh
thisdir=$(dirname "$0")
. "$thisdir/utils.sh"

let iparams=$#
#echo "num of params:" $iparams

# compruebo si hay argumentos
(( isargsok = iparams>0 ? 1 : 0 ))
#echo "isargsok" $isargsok

if (( !isargsok ))
then 
  echo "no argumentes passed. Try: -m \"some message\""
  exit
fi

while (( isargsok ));
do
  case $1 in
    m=*)
      m="${1#*=}"
    ;;  
    p=*)
      # no se para que es p ^^
      p="${1#*=}"
    ;;
    *)

    msg=$(echo $m | xargs echo -n)
    isize=${#msg}
    if [[ $isize -gt 0 ]] 
    then
      # si hay parametro project
      
      if [[ ! -z "$p" ]]; then
        fullpath="/e/projects/prj_$p"
        if is_ios; then fullpath=$PATHPRJ"/prj_$p"; fi

        if [[ ! -d $fullpath ]]; then 
          echo "not dir: $fullpath"          
          exit 1
        fi      
        cd $fullpath
      fi

      if [[ "$PWD" == *"prj_compass"* ]]; then
        echo "forbidden push for compass repository"
        exit 1
      fi

      echo "..commiting"
      git add --all; git commit -m "$msg"; git push;
      exit 0
    fi

    printf "*************************************\n"
    printf "* mygit.sh  Error: Invalid argument.*\n"
    printf "*************************************\n"
    exit 1
    esac
    shift
done