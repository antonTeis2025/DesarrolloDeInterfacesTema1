Una message box sirve para dar un aviso al usuario. Pueden ser de aviso, informativas, errores....

Se crean de la siguiente manera:

```python
# Creamos un objeto QMessageBox
msg = QtWidgets.QMessageBox()
# La establecemos en modo modal (bloquea el resto de ventanas) 
msg.setModal(True)  
# Establecemos un titulo de ventana
msg.setWindowTitle("Listo")  
# icono informativo
msg.setIcon(QtWidgets.QMessageBox.Icon.Information)  
# Establecemos mensaje
msg.setText("Copia creada correctamente")  
# Ejecutamos
msg.exec()
```