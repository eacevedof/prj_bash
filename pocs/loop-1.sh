#!/usr/local/bin/bash

for num in 1 2 3 4 5
do
	echo "number $num"
done

# loop todos los directorios
pathdir=$PATHPRJ
for file in $(ls $pathdir) 
do
	echo "check file $pathdir/$file"
	if [ ! -d "$pathdir/$file" ]; then
		continue
	fi
	echo "is a dir $file"
done


for file in $(ls ./*); do if [ ! -d "./$file" ]; then continue; fi done

#for num in 1 2 3; do echo "number i $num"; done
