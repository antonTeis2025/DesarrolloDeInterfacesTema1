from PyQt5 import QtWidgets

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
            result = var.dlgSalir.exec_()
            if result == QtWidgets.QDialog.Accepted:
                print("Saliendo...")
                sys.exit()

        except Exception as error:
            print("Error ", error)

    def abrirCalendar():
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print("Error ", error)

    def cargarFecha(qDate):
        try:
            # Convertimos el argumento de la función, que es tipo qDate, a string
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            # Ponemos el texto de la fecha de hoy (variable data) en el line edit para la fecha
            var.ui.txtFecha.setText(str(data))
            # Ocultamos el QtDialog del calendario
            var.dlgcalendar.hide()
        except Exception as error:
            print("Error ", error)