![[Pasted image 20251111202033.png]]
Son ventanas que salen en la aplicación para que el usuario tenga que hacer **una accion concreta**.

Para que una ventana sea modal debe activarse la opción modal:
![[Pasted image 20251111204446.png]]

---
En nuestro programa, la ventana principal es un objeto tipo **QMainWindow**, y las ventanas modales son un objeto **QDialog**. 

Primero, creamos la ventana en QtDesigner y la compilamos. (confirmacion_salida)

Para poder implementarla en nuestro código, al cargar la aplicación:
```python
# Cargamos el menú de salir a una variable global  
var.avisosalir = confirmacion_salida.Ui_Dialog()  
# Creamos un QtDialog en una variable global, para que salga como ventana de confirmacion  
var.dlgSalir = QtWidgets.QDialog()  
# Hacemos el setupUI con el dialogo como argumento  
var.avisosalir.setupUi(var.dlgSalir)
```
Creamos el método salir para que muestre la ventana al pulsar el botón salir
```python
def Salir():  
    try: 
	    # Creamos una variable que sea el objeto diaglogo.exec_() 
        result = var.dlgSalir.exec_()  
        if result == QtWidgets.QDialog.Accepted:  
	        # Si se pulsa aceptar, salir
            print("Saliendo...")  
            sys.exit()  
  
    except Exception as error:  
        print("Error ", error)
```
Asignamos el metodo a un botón, en este caso el del menú:
```python
var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
```