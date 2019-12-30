# prj_bash
Bash scripting 

### **`if then else`**
- `read mivar` espera el prompt a que se guarde en mivar
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