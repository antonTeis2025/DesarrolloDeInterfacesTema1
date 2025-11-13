import datetime
import os
import shutil
import zipfile

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

import conexion
import var
import sys

class Eventos():

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
                # Creamos un fichero zip con el nombre de la fecha
                archivoZip = zipfile.ZipFile(nombre, 'w')
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

    def cargaProvincias():
        # Necesita siempre el primer elemento vacío porque es el que muestra
        provincias = ['', 'Pontevedra', 'Lugo', 'Orense', 'A Coruña']
        try:
            for i in provincias:
                var.ui.comboBoxProvincias.addItem(i)
        except Exception as error:
            print("Error ", error)

    def Saludo():

        try:

            var.ui.label.setText("Saludo")

        except Exception as error:
            print("Error ", error)

    def Salir():
        try:
            result = var.dlgSalir.exec()
            if result == QtWidgets.QDialog.DialogCode.Accepted:
                print("Saliendo...")
                sys.exit()

        except Exception as error:
            print("Error ", error)

    def abrirCalendar():
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print("Error ", error)

