#!/bin/bash
#loop-2.sh

pathdir=$PATHPRJ
# carpetas que no se tomarán en cuenta
arexclude=("temper" "lacia" "tmp")

for file in $(ls $pathdir) 
do
	pathfile="$pathdir/$file"
	if [[ ${arexclude[*]} =~ $file ]]; then continue; fi
	
	if [ ! -d $pathfile ]; then
		continue
	fi
	# el fichero es un dicrectorio por lo tanto se puede ejecutar
	# cualquier comando con esta ruta. por ejemplo un ls 
	# -e permite entender \n como salto de linea
	echo -e "\n===========\n$pathfile is a dir\n==========\n"
	ls $pathfile
done
