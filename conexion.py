from PyQt5 import QtSql
from PyQt5.uic.Compiler.qtproxies import QtWidgets

import var
import os

class Conexion():
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