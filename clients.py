from PyQt6 import QtWidgets

import conexion
import var

class Customers:


    def limpiarCliente():
        # Diccionario de campos de texto de los clientes
        textos_cliente = [
            var.ui.txtFecha,
            var.ui.txtDniCli,
            var.ui.txtNombreCli,
            var.ui.txtApelidosCli
        ]
        # Establecemos que los radio buttons no sean exclusivos
        var.ui.rbtHombre.setAutoExclusive(False)
        var.ui.rbtMujer.setAutoExclusive(False)
        var.ui.rbtHombre.setChecked(False)
        var.ui.rbtMujer.setChecked(False)
        # Los volvemos a hacer exclusivos
        var.ui.rbtHombre.setAutoExclusive(True)
        var.ui.rbtMujer.setAutoExclusive(True)
        # Limpiar checkboxes
        var.ui.cbEfectivo.setChecked(False)
        var.ui.cbTransferencia.setChecked(False)
        var.ui.cbTarjeta.setChecked(False)
        # Limpiar campos de texto
        for i in textos_cliente:
            i.setText('')

    def selProvincia(provincia):
        print("Has seleccionado la provincia: ", provincia)
        var.provincia = provincia

    def selPago():
        try:
            var.pay = [] # Vaciamos la lista de los metodos de pago
            for i, data in enumerate(var.ui.buttonGroup.buttons()): # checkBoxPago es un grupo de botones
                if data.isChecked() and i == 2:
                    print("Paga en efectivo")
                    var.pay.append("Efectivo")
                if data.isChecked() and i == 0:
                    print("Paga en tarjeta")
                    var.pay.append("Tarjeta")
                if data.isChecked() and i == 1:
                    print("Paga en transferencia")
                    var.pay.append("Transferencia")

        except Exception as error:
            print("Error ", error)
        return var.pay

    def selSexo():
        global sex
        if var.ui.rbtHombre.isChecked():
            print("Soy hombre")
            sex = "Hombre"
        if var.ui.rbtMujer.isChecked():
            print("Soy mujer")
            sex = "Mujer"

    def checkDni(self=None):
        try:
            # evita el problema de ejecutar varios editinFinised O QUITAR SETFOCUS
            var.ui.txtDniCli.editingFinished.disconnect(Customers.checkDni)
            dni = var.ui.txtDniCli.text()
            dni = str(dni).upper()
            var.ui.txtDniCli.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.txtDniCli.setStyleSheet('background-color: rgb(255, 255, 220);')
                else:
                    var.ui.txtDniCli.setStyleSheet('background-color:#FFC0CB;')
                    var.ui.txtDniCli.setText(None)
                    var.ui.txtDniCli.setPlaceholderText("Invalid DNI/NIE")
                    var.ui.txtDniCli.setFocus()
            else:
                var.ui.txtDniCli.setStyleSheet('background-color:#FFC0CB;')
                var.ui.txtDniCli.setText(None)
                var.ui.txtDniCli.setPlaceholderText("Invalid DNI/NIE")
                var.ui.txtDniCli.setFocus()
        except Exception as error:
            print("error en validar dni ", error)
        finally:
            var.ui.txtDniCli.editingFinished.connect(Customers.checkDni)

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

    def datosCliente():
        try:
            # Creamos el diccionario cliente con todos los valores escritos de los campos del formulario
            cliente = [
                var.ui.txtDniCli.text(),
                var.ui.txtApelidosCli.text() ,
                var.ui.txtNombreCli.text() ,
                var.ui.txtFecha.text(),
                var.provincia
            ]
            # Cargamos la lista de los metodos de pago que ha usado el cliente
            var.pay2 = Customers.selPago()
            # Añadimos la variable global que guarda su sexo
            cliente.append(sex)
            # Añadimos la lista de pagos al diccionario cliente
            cliente.append(var.pay2)
            # Probamos a imprimir el cliente para ver si está to bien
            print(cliente)
            # Limpiamos la lista de pagos
            var.pay = []
            # Devolvemos el diccionario con los datos del cliente
            return cliente
        except Exception as error:
            print("Error ", error)

    def modificaCliente():
        cliente = Customers.datosCliente()
        conexion.Conexion.actualizaCliente(cliente)

    def insertarCliente():
        try:
            # Creamos un diccionario vacio que será el que insertemos en la tabla
            # insertar = []
            # Conseguimos la lista de datos del cliente
            cliente = Customers.datosCliente()
            # Insertamos los 3 primeros datos de cliente (DNI, apellidos y nombre) al diccionario que se insertara
            # insertar.append(cliente[0])
            # insertar.append(cliente[1])
            # insertar.append(cliente[2])

            # row = 0 # Posicion de la fila para que inserte arriba de to
            # column = 0 # Posicion de la columna
            # var.ui.tablaClientes.insertRow(row) # Añade una fila a la tabla
            #    for registro in insertar:
            #        # cada celda tiene una posición (fila, columna) y cargamos el dato
            #        cell = QtWidgets.QTableWidgetItem(registro) # Creamos un objeto tipo celda de QTable
            #        var.ui.tablaClientes.setItem(row, column, cell) # Escribe el dato cell en la posicion row, column
            #        column+=1 # Suma 1 para ir a la siguiente columna a insertar el siguiente registro
            #    print(cliente)
            conexion.Conexion.insertarCliente(cliente)

        except Exception as error:
            print("Error ", error)

    def cargarCliente():
        try:
            # Antes de cargar nada limpiamos todos los campos para evitar errores
            Customers.limpiarCliente()
            # Cargamos a la variable fila los valores de la fila seleccionada de la tabla
            # !! Esta fila es una lista de objetos tipo QTableWidgetItem, no de strings
            fila = var.ui.tablaClientes.selectedItems()
            if fila: # Si la fila no está vacía...
                # Extraemos el texto de cada objeto del diccionario
                fila = [dato.text() for dato in fila]
            # Imprimimos la fila para ver que to esté bien
            print(fila)
            # La columna 0 es siempre el DNI
            dni = fila[0]
            # IMPORTANTE guardamos el oldDni para actualizar los otros datos
            var.oldDni = dni
            # Llamamos a la BBDD para que consulte los datos del cliente por su DNI
            datosCliente = conexion.Conexion.datosCliente(dni)

            # Asignar a cada campos su valor
            var.ui.txtDniCli.setText(str(datosCliente[0]))
            var.ui.txtApelidosCli.setText(str(datosCliente[1]))
            var.ui.txtNombreCli.setText(str(datosCliente[2]))
            var.ui.comboBoxProvincias.setCurrentText(str(datosCliente[3]))
            if (datosCliente[4] == "Mujer"):
                var.ui.rbtMujer.setChecked(True)
            else:
                var.ui.rbtHombre.setChecked(True)
            var.ui.txtFecha.setText(str(datosCliente[5]))
            pagos = datosCliente[6]
            if 'Transferencia' in pagos:
                var.ui.cbTransferencia.setChecked(True)
            if 'Efectivo' in pagos:
                var.ui.cbEfectivo.setChecked(True)
            if 'Tarjeta' in pagos:
                var.ui.cbTarjeta.setChecked(True)


        except Exception as e:
            print("Error ", e)

    def bajaCliente():
        try:
            # Recoge el campo DNI (clave unica para cada cliente)
            dni = var.ui.txtDniCli.text()
            # DELETE FROM cliente WHERE dni =
            conexion.Conexion.borraCliente(dni)
            # Recarga la lista de clientes a la tabla
            conexion.Conexion.cargarClientesTabla()
            # Limpia los campos de input
            Customers.limpiarCliente()

        except Exception as error:
            print("Error ", error)

