#!/bin/bash

# loop todos los directorios
pathdir=$PATHPRJ
for file in $(ls $pathdir) 
do
	echo "check if file $pathdir/$file is dir"
	if [ ! -d "$pathdir/$file" ]; then
		continue
	fi
	echo "is a dir $file"
done

# loop en una linea
for file in $(ls ./*); do if [ ! -d "./$file" ]; then continue; fi done

