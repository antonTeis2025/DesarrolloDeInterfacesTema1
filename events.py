from PyQt6 import QtWidgets

import var
import sys

class Eventos():

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

