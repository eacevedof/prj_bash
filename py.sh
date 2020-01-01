#!/bin/sh

# py.sh <path-script> 

thispath=$(dirname "$0")
# echo $thispath
#exit
pypath="$thispath/py/console.py"
#echo $pypath
# dirname "$0"

#format index
module=$([ -z "$1" ] && echo "udemy" || echo "$1")
action=$([ -z "$2" ] && echo "index" || echo "$2")

py $pypath $module $action