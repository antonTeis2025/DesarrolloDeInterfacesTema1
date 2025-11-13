import datetime
import os

from PyQt6 import QtSql
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import var

class Printer():
    def reportListaClientes():
        try:
            # Creamos el canvas en la carpeta reports
            var.report = canvas.Canvas("informes/report.pdf", pagesize=A4)

            # Ponemos la cabecera
            Printer.cabecera()

            # Dibujamos el string Listado de clientes en esa posicion x y
            var.report.drawString(255, 735, 'Listado de clientes')

            # Linea despues del titulo del documento
            var.report.line(45, 730, 525, 730)

            # Campos del cliente
            var.report.drawString(45, 710, "Codigo")
            var.report.drawString(90, 710, "DNI")
            var.report.drawString(180, 710, "Apelidos")
            var.report.drawString(325, 710, "Nome")
            var.report.drawString(465, 710, "Fecha alta")
            # Linea separadora
            var.report.line(45, 703, 525, 703)


            # Preparamos la query
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codigo, dni, apellidos, nombre, fechaalta"
                          " FROM clientes"
                          " ORDER BY apellidos, nombre")

            # Cambiar el tamaño de la fuente
            var.report.setFont('Helvetica', size=10)

            if query.exec():
                # Coordenadas en el papel para empezar a poner los datos
                i = 50
                j = 690
                # Por cada dato en la query, dibuja los datos en el reporte
                while query.next():
                    var.report.drawString(i, j, str(query.value(0)))
                    var.report.drawString(i+30, j, str(query.value(1)))
                    var.report.drawString(i+130, j, str(query.value(2)))
                    var.report.drawString(i+280, j, str(query.value(3)))
                    var.report.drawString(i+418, j, str(query.value(4)))
                    # Restamos a coordenada J para que escriba debajo
                    j -= 30

            # Ponemos el pie
            Printer.pie("LISTADO CLIENTES")
            # Guardamos
            var.report.save()

            # Recorremos la carpeta informes abriendo todos los ficheros PDF
            rootPath = ".\\informes"
            for file in os.listdir(rootPath):
                if file.endswith(".pdf"):
                    os.startfile(os.path.join(rootPath, file))

        except Exception as e:
            print("Error al generar report: ", e)

    def cabecera():
        try:
            logo = '.\\img\\logo.jpg'
            # definimos titulo, autor y fuente tipografica
            var.report.setTitle("INFORMES")
            var.report.setAuthor("Anton")
            var.report.setFont("Helvetica", size=10)

            # colocamos lineas para delimitar la cabecera
            var.report.line(45, 820, 525, 820)
            var.report.line(45, 745, 525, 745)

            # Colocamos datos de la empresa
            var.report.drawString(50, 805, "00000000T") # NIF
            var.report.drawString(50, 790, "IES Teis, S.L.") # Nombre empresa
            var.report.drawString(50, 775, "Avenida de Galicia 101 - Vigo") # Direccion
            var.report.drawString(50, 760, "+34 123 45 67 89") # telefono

            # Insertamos el logo
            var.report.drawImage(logo, 450, 752)

        except Exception as e:
            print("Error al generar cabecera del report: ", e)

    @staticmethod
    def pie(nombreInforme):
        try:
            # Insertar linea separadora
            var.report.line(50, 50, 525, 50)
            # Conseguimos la fecha y la formateamos
            fecha = datetime.datetime.today()
            fecha = fecha.strftime("%d/%m/%Y %H:%M:%S")

            # Ponemos otra fuente para el pie de pagina
            var.report.setFont("Helvetica-Oblique", size=7)

            # Dibujar fecha
            var.report.drawString(460, 40, str(fecha))
            # Dibujar numero de pagina
            var.report.drawString(275, 40, str('Pagina %s' % var.report.getPageNumber()))
            # Dibujar nombre del informe
            var.report.drawString(50, 40, str(nombreInforme))
        except Exception as e:
            print("Error en el pie del report: ", e)