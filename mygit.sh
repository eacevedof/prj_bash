#!/bin/sh


# [[ $# -gt 0 ]]; mibool=$? # OK 1 si no hay argumentos 0 en caso contrario
# [[ $# -gt 0 ]];mibool=$? # OK mismo que el anterior
[[ $# -gt 0 ]]; let mibool=$? # OK similar al anterior

# mibool=$([ $# -gt 0 ] && echo 1 || echo 0) # OK

# [[$# -gt 0]];mibool=$? # NO! hay que respetar los espacios entre corchetes
# con operador ternario

# mibool='[[ $# -gt 0 ]]'  NO! guarda un string
# mibool=$([[ $# -gt 0 ]]) NO da erro pero no se guarda nada

# [[$# -gt 0]]; mibool=$? NO!
# mibool=[[ $# -gt 0 ]];  NO!

echo "mibool" $mibool
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