Permite escoger solamente un elemento de varios radio buttons.
![[Pasted image 20251111190159.png]]

---
Cada vez que se marcan o desmarcan, emiten una señal toggled tipo boolean. Si queremos ejecutar una funcion cada vez que ocurre esto:
```python
elemento.toggled.connect(funcion)
```
Después, en la función que llamaremos, podemos validar si ha sido seleccionado con:
```python
elemento.isChecked() # True -> marcado
```

---
Si tenemos varios radiobutton, lo que se suele hacer es hacer una lista con ellos y pasarles a todos la misma función, con isChecked dentro para saber cual de ellos se presionó.
```python
var.rbtsexo = (var.ui.rbtHombre, var.ui.rbtMujer)  
for i in var.rbtsexo:  
    i.toggled.connect(clients.Customers.selSexo)
```
La función selSexo:
```python
def selSexo():  
    if var.ui.rbtHombre.isChecked():  
        print("Soy hombre")  
    if var.ui.rbtMujer.isChecked():  
        print("Soy mujer")
```
