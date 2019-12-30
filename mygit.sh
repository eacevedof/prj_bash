#!/bin/sh

# [ -z "foo" ]; r=$?
#miv='[ $# -gt 0 ]'
[ $# -gt 0 ] miv=$?

echo "miv" $miv

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