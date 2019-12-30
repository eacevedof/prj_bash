#!/bin/sh

echo $1 
echo $2

read someparam
echo someparam
echo $someparam

while [ $# -gt 0 ]; do
	case "$1" in
		--m=*)
			m="${1#*=}"
			;;
		--arg_1=*)
			arg_1="${1#*=}"
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