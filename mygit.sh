#!/bin/sh

let iparams=$#
echo "num of params:" $iparams
(( isargsok = iparams>0 ? 1 : 0 ))
echo "isargsok" $isargsok

exit
while [ $# -gt 0 ]; do
	case "$1" in
		-a=*)
			a="${1#*=}"
      echo ${a}
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