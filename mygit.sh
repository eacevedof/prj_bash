#!/bin/sh

let iparams=$#
echo "num of params:" $iparams

# seteo
(( isargsok = iparams>0 ? 1 : 0 ))
echo "isargsok" $isargsok

# while [[ "$isargsok" -eq 1 ]]; # ok
while (( isargsok ));
do
	case "$1" in
		-a=*)
			a="${1#*=}"
      echo ${a}
      exit
			;;
		-b=*)
			b="${1#*=}"
      echo ${b}
			;;
		*)
    printf "***************************\n"
    printf "* Error: Invalid argument.*\n"
    printf "***************************\n"
    exit 1
	esac
	shift
done

# git add --all; git commit -m "mygit.sh"; git push;