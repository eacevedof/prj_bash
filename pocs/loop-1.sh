for num in 1 2 3 4 5
do
	echo "number $num"
done

for file in $(ls ./*) 
do
	if [ -d "$file" ]; then
		echo "$file is a dir"
	fi
done
