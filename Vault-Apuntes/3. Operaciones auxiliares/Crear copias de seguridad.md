Haremos una funcion que se llame `crearBackup()` en events.py:

```python
def crearBackup():  
    try:  
        # Creamos una variable para el nombre del fichero por defecto que sea la fecha de hoy  
        fecha = datetime.datetime.now()  
        fecha = fecha.strftime("%d_%m_%Y %H-%M-%S")  
        nombre = str(fecha)+"_backup.zip"  
        # Abrimos el dialogo para asignar tanto el directorio como el nombre del fichero  
        directorio, nombreFichero = var.dlgAbrir.getSaveFileName(  
            None,  
            "Guardar copia", # Nombre ventana  
            nombre, # Nombre por defecto fichero  
            ".zip" # Extension a la que se guardara  
        )  
        if var.dlgAbrir.accept and nombreFichero != "": # Si el usuario acepta...  
            # Creamos un fichero zip con el nombre de la fecha            archivoZip = zipfile.ZipFile(nombre, 'w')  
            # Escribimos en el zip el fichero de BBDD, con output en su ruta base y en modo deflated  
            archivoZip.write(var.dbfile, os.path.basename(var.dbfile), zipfile.ZIP_DEFLATED)  
            # Cerramos el zip  
            archivoZip.close()  
            # Movemos el archivo al directorio especificado en el dialogo  
            shutil.move(str(nombre), str(directorio))  
            # Mostramos al usuario una ventana para decir que ya se creo  
            msg = QtWidgets.QMessageBox()  
            msg.setModal(True)  
            msg.setWindowTitle("Listo")  
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)  
            msg.setText("Copia creada correctamente")  
            msg.exec()  
    except Exception as error:  
        print("Error al hacer backup ", error)
```

La llamamos desde un boton de backup desde main

```python
# Conectado boton de copia de seguridad  
var.ui.botBackup.clicked.connect(events.Eventos.crearBackup)
```