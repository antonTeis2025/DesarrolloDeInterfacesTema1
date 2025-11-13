from PyQt6 import QtSql
from PyQt6 import QtWidgets

import var
import os

class Conexion():

    def cargarClientesTabla():
        # Preparamos una query
        query = QtSql.QSqlQuery()
        query.prepare("SELECT dni, apellidos, nombre FROM clientes")
        # Ejecutamos la query
        if query.exec():
            # Limpiamos la tabla para asegurarnos
            var.ui.tablaClientes.clearContents()
            var.ui.tablaClientes.setRowCount(0)
            index = 0 # Creamos un indice para insertar en la tabla de la UI
            # Mientras la query tenga siguiente dato:
            while query.next():
                # query.value -> [dni, apellidos, nombre]
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)

                var.ui.tablaClientes.setRowCount(index+1) # Crea la fila
                # setItem(fila, columna, valor (objeto QTableWidgetItem))
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(dni)))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(apellidos)))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(nombre)))
                # Pasa a la siguiente fila
                index += 1


    @staticmethod
    def insertarCliente(cliente):
        query = QtSql.QSqlQuery()
        # Preparamos la query
        query.prepare("INSERT INTO clientes (dni, apellidos, nombre, fechaalta, provincia, sexo, formaspago)"
                      " VALUES (:dni, :apellidos, :nombre, :fechaalta, :provincia, :sexo, :formaspago)")
        # Sustituimos los valores con bindValue() para evitar SQLi
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':fechaalta', str(cliente[3]))
        query.bindValue(':provincia', str(cliente[4]))
        query.bindValue(':sexo', str(cliente[5]))
        query.bindValue(':formaspago', str(cliente[6]))

        if query.exec():
            print("[+] Insercion correcta de ", cliente)
            Conexion.cargarClientesTabla()
        else:
            print("Error ", query.lastError().text())

    def db_connection(self):
        # Comprobamos que existe el archivo de BBDD
        if not os.path.exists(var.dbfile):
            QtWidgets.QMessageBox.critical(None,
                                           'Error hermano',
                                           'Hermano no quería ser yo el que lo diga, pero no existe el fichero de configuracion de la base de datos.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel
            )
            return False
        # Conexion con BBDD sqlite
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.dbfile)

        if db.open():
            # Consulta para ver si hay tablas
            query = QtSql.QSqlQuery()
            query.exec("SELECT name FROM sqlite_master WHERE type='table'")

            # Si NO hay tablas
            if not query.next():
                QtWidgets.QMessageBox.critical(None,
                                               'Error hermano',
                                               'Hermano no quería ser yo el que lo diga, pero tu base de datos está putamente sin tablas.',
                                               QtWidgets.QMessageBox.StandardButton.Cancel
                                               )
                return False
            else:
                print("[+] Conexión correcta a la BBDD")
                return True
        else:
            QtWidgets.QMessageBox.critical(None,
                                           'Error hermano',
                                           'Hermano no quería ser yo el que lo diga, pero ha habido un error extraño en tu conexion con la BBDD',
                                           QtWidgets.QMessageBox.StandardButton.Cancel
                                           )
            return False

    @staticmethod
    def borraCliente(dni):
        query = QtSql.QSqlQuery()
        # Preparamos query
        query.prepare("DELETE FROM clientes WHERE dni=:dni")
        # Ponemos el valor del DNI en la query
        query.bindValue(':dni', str(dni))
        # Ejecutamos, y si es correcto damos mensaje
        if query.exec():
            print("[+] Cliente con DNI " + str(dni) + " eliminado correctamente")
        else:
            print("[+] No se pudo borrar cliente con DNI " + str(dni))

    @staticmethod
    def datosCliente(dni):
        # Creamos un diccionario, que sera el return
        result = []

        # Preparar query
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM clientes WHERE dni=:dni")
        query.bindValue(':dni', str(dni))

        if query.exec():
            if query.next():
                # Cada fila tiene 8 elementos, 7 sin contar el ID (elemento 0)
                elemento = 1 # Empezariamos en el elemento 1 (dni)
                while elemento<=7:
                    result.append(query.value(elemento))
                    elemento += 1
            else:
                print("[+] Cliente no existe")
        else:
            print("[!] No se pudo ejecutar la query")

        print("Resultado de datos cliente: ", result)
        return result

    @staticmethod
    def actualizaCliente(cliente):
        query = QtSql.QSqlQuery()
        # Preparamos la query
        query.prepare("UPDATE clientes SET "
                      "dni = :dni, "
                      "apellidos = :apellidos, "
                      "nombre = :nombre, "
                      "fechaalta = :fechaalta, "
                      "provincia = :provincia, "
                      "sexo = :sexo, "
                      "formaspago = :formaspago "
                      "WHERE dni = :oldDni")
        # Sustituimos los valores con bindValue() para evitar SQLi
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':fechaalta', str(cliente[3]))
        query.bindValue(':provincia', str(cliente[4]))
        query.bindValue(':sexo', str(cliente[5]))
        query.bindValue(':formaspago', str(cliente[6]))
        query.bindValue(':oldDni', var.oldDni)

        if query.exec():
            print("[+] Actualizacion correcta de ", cliente)
            Conexion.cargarClientesTabla()
        else:
            print("Error ", query.lastError().text())