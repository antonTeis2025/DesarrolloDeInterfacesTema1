![[Pasted image 20251111202033.png]]
Son ventanas que salen en la aplicación para que el usuario tenga que hacer **una accion concreta**.

Para que una ventana sea modal debe activarse la opción modal:
![[Pasted image 20251111204446.png]]

---
En nuestro programa, la ventana principal es un objeto tipo **QMainWindow**, y las ventanas modales son un objeto **QDialog**. 

Para poder implementarla en nuestro código, al cargar la aplicación:
```python
# Cargamos el menú de salir a una variable global  
var.avisosalir = confirmacion_salida.Ui_Dialog()  
# Creamos un QtDialog, para que salga como ventana de confirmacion  
var.dlgSalir = QtWidgets.QDialog()  
# Hacemos el setupUI con el dialogo como argumento  
var.avisosalir.setupUi(var.dlgSalir)
```