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
### Guardar valores de retorno
```sh
```s
# If you want to store the return code from a command in a variable you can do
/bin/true
ret=$?

# if you want to store the output from a command in a variable you can do
out=$(/bin/true)
```

#### **asignar booleanos**
- cuando se compara se usan los corchetes (square brackets) que estos son un atajo a la **función test**
- asignar una expresion booleana a una variable
- **$#** no es un párametro simple, es un comando
```sh
# casos OK
[[ $# -gt 0 ]]; mibool=$? # OK 1 si no hay argumentos 0 en caso contrario
[[ $# -gt 0 ]];mibool=$? # OK mismo que el anterior
[[ $# -gt 0 ]]; let mibool=$? # OK similar al anterior

# con operador ternario
# https://stackoverflow.com/questions/3953645/ternary-operator-in-bash
mibool=$([ $# -gt 0 ] && echo 1 || echo 0) # OK invirtiendo lo que deuvele test
mibool=$([[ $# -gt 0 ]] && echo 1 || echo 0) # OK

##########
# casos NOK
[[$# -gt 0]];mibool=$? # NO! hay que respetar los espacios entre corchetes
mibool='[[ $# -gt 0 ]]'  # NO! guarda un string
mibool=$([[ $# -gt 0 ]]) # NO da error pero no se guarda nada

[[$# -gt 0]]; mibool=$? # NO!
mibool=[[ $# -gt 0 ]];  # NO!
(( mibool = [ $# -gt 0 ] ? 1 : 0 )) # NO
(( [ $# -gt 0 ] ? (mibool=1) : (mibool=0) )) # NO
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
#### **condición en while**
```sh
#!/bin/sh
isargsok=1
# while [[ "$isargsok" -eq 1 ]]; # ok
while (( isargsok )); #ok
do
  echo $isargsok
  exit
done
```