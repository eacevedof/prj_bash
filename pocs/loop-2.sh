#!/bin/bash
#loop-2.sh

# $PATHPRJ variable de entorno que tiene una ruta como /my-space/projects
pathdir=$PATHPRJ
# carpetas que no se tomarán en cuenta
arexclude=("temper" "lacia" "tmp")

for file in $(ls $pathdir) 
do
	# si el nombre del archivo está en los strings excluidos salta al siguiente valor
	if [[ ${arexclude[*]} =~ $file ]]; then continue; fi
	
	pathfile="$pathdir/$file"	
	# si el archivo no es un directorio salta al siguiente valor
	if [ ! -d $pathfile ]; then continue; fi

	# el fichero es un dicrectorio por lo tanto se puede ejecutar
	# cualquier comando con esta ruta. por ejemplo un ls 
	# -e permite entender \n como salto de linea
	echo -e "\n===========\n$pathfile is a dir\n==========\n"
	ls -lat $pathfile
done
