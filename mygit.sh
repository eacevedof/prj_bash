#!/bin/sh
# automatiza el push total de la carpeta donde estoy
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
		-m=*)
			m="${1#*=}"
			;;
		--m=*)
			m="${1#*=}"
			;;
		*)
    msg=$(echo $m | xargs echo -n)
    isize=${#msg}
    if [[ isize > 0 ]] 
    then
      echo "commiting"
      git add --all; git commit -m "mygit.sh"; git push;
    fi
    exit 0

    printf "***************************\n"
    printf "* Error: Invalid argument.*\n"
    printf "***************************\n"
    exit 1
	esac
	shift
done