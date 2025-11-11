Permite seleccionar varias opciones marcando las casillas.
![[Pasted image 20251111190312.png]]

---
Cada vez que se marcan o desmarcan, emiten una señal stateChanged, a la que le podemos asignar un evento.
```python
elemento.stateChanged(funcion)
```
Desde el código, podemos validar si ha sido seleccionado con:
```python
elemento.isChecked() # True -> marcado
```
Podemos también hacer que estén checkeadas
```python
elemento.setChecked(True) # Marcar
elemento.setChecked(False) # Desmarcar
```

---
Al igual que con los radio buttons, se suelen meter en una lista para pasarle a todos la misma funcion en la que se comprueba con isChecked cuales están marcadas.
```python
# Guardamos todos los checkbox en una lista  
var.cbpago = (var.ui.cbTarjeta, var.ui.cbEfectivo, var.ui.cbTransferencia)  
for i in var.cbpago:  
    # Hacemos que por cada actualización, se ejecute selPago
    i.stateChanged.connect(clients.Customers.selPago)
```
Funcion selPago:
```python
def selPago():  
    print()  
    if var.ui.cbTarjeta.isChecked():  
        print("pago con tarjeta")  
    if var.ui.cbEfectivo.isChecked():  
        print("pago en efectivo")  
    if var.ui.cbTransferencia.isChecked():  
        print("pago con transferencia")
```