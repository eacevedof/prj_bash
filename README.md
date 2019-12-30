# prj_bash
Bash scripting 

## TIPS
### Obtener el numero de argumentos al llamar al bash
- `$#` devuelve la longitud de argumentos pasados al fichero
```sh
#!/bin/sh
# fichero: mybash.sh
echo $#
```
- Ejemplo
```sh
mybash.sh xxx  # devolveria 1

mygit.sh aaa yyyy xx "zz vv ii" 1246 6.689 z v i
9
```

#### **asignar booleanos**
```s
# If you want to store the return code from a command in a variable you can do

/bin/true
ret=$?

# if you want to store the output from a command in a variable you can do
out=$(/bin/true)
```



#### **`if then else`**
- `read mivar` 
	- espera el prompt a que se escriba algo para que a posteriori se guarde en mivar
```s
echo ' Adivina el valor numerico de la variable'
read A

if [ $A = 1 ]; then
	echo 'Has acertado'
	exit 0
else
	echo 'Error, te has equivocado'
exit
fi
```