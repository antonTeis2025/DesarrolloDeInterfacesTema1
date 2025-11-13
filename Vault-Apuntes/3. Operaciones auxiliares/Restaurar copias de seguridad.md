Para restaurar las copias, necesitamos hacer una funcion que **pida al usuario el archivo de copia**, para después **descomprimir el archivo y recargar la conexion y tablas del programa**.

Queda algo así:

```python
    def restaurarBackup():
        try:
            # esta variable almacena una lista de archivos (por si multiseleccionas)
            nombreArchivo = var.dlgAbrir.getOpenFileName(
                None,
                "Restaurar Copia de seguridad", # titulo de la ventana
                "", # Nombre predeterminado (vacio)
                "*.zip;;All Files (*)" # Formatos validos
            )
            if var.dlgAbrir.accept and nombreArchivo != "":
                # Nos quedamos con el primero (solo deberia seleccionarse uno)
                archivo = nombreArchivo[0]
                # Extraemos el archivo
                with zipfile.ZipFile(archivo, 'r') as archivoZip:
                    archivoZip.extractall(pwd=None)
                # Cerramos el zip
                archivoZip.close()

                # Recreamos la conexion con la nueva BBDD
                conexion.Conexion.db_connection()
                # Actualizamos la tabla
                conexion.Conexion.cargarClientesTabla()
                # Ejecutamos una messageBox para informar de que está restaurada la copia
                # Creamos un objeto QMessageBox
                msg = QtWidgets.QMessageBox()
                # La establecemos en modo modal (bloquea el resto de ventanas)
                msg.setModal(True)
                # Establecemos un titulo de ventana
                msg.setWindowTitle("Listo")
                # icono informativo
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                # Establecemos mensaje
                msg.setText("Copia restaurada correctamente")
                # Ejecutamos
                msg.exec()

        except:
            print("Error al restaurar backup ", sys.exc_info()[0])
```

Lo asignare a un boton de la toolbar desde main:

```python
# Conectado boton toolbar restaurar copia  
var.ui.actionRestaurar.triggered.connect(events.Eventos.restaurarBackup)
```