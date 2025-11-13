El cuadro combinado, combo box o lista desplegable es un campo que permite seleccionar un elemento de una lista de posibles valores.
![[Pasted image 20251111195129.png]]

---
Para **cargar datos** a la ComboBox, lo haremos mediante iterar array ejecutando addItem por cada elemento.
```python
def cargaProvincias():  
    # Necesita siempre el primer elemento vacío porque es el que muestra  
    provincias = ['', 'Pontevedra', 'Lugo', 'Orense', 'A Coruña']  
    try:  
        for i in provincias:  
            var.ui.comboBoxProvincias.addItem(i)  
    except Exception as error:  
        print("Error ", error)
```
Para **leer el dato seleccionado** usamos el trigger ``activated``, con ``[str]`` para que lo devuelva en texto plano.

```python
var.ui.comboBoxProvincias.activated[str].connect(clients.Customers.selProvincia)
```
	!! EN PYQT6 es así
	textActivated.connect()

La función selProvincia recibe como argumento la salida de ``activated[str]``, que es la provincia en texto plano

```python
def selProvincia(provincia):  
    print("Has seleccionado la provincia: ", provincia)
```

Si queremos que la combobox **seleccione un elemento ya definido** lo haremos con:

```python
var.ui.comboBoxProvincias.setCurrentText("Pontevedra")
```
