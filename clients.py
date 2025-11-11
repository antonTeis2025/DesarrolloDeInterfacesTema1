import var

class Customers:


    def limpiarCliente():
        textos_cliente = [
            var.ui.txtDniCli,
            var.ui.txtNombreCli,
            var.ui.txtApelidosCli
        ]

        var.ui.rbtHombre.setChecked(False)
        var.ui.rbtMujer.setChecked(False)
        var.ui.cbEfectivo.setChecked(False)
        var.ui.cbTransferencia.setChecked(False)
        var.ui.cbEfectivo.setChecked(False)
        for i in textos_cliente:
            i.setText('')

    def selProvincia(provincia):
        print("Has seleccionado la provincia: ", provincia)

    def selPago():
        print()
        if var.ui.cbTarjeta.isChecked():
            print("pago con tarjeta")
        if var.ui.cbEfectivo.isChecked():
            print("pago en efectivo")
        if var.ui.cbTransferencia.isChecked():
            print("pago con transferencia")

    def selSexo():
        if var.ui.rbtHombre.isChecked():
            print("Soy hombre")
        if var.ui.rbtMujer.isChecked():
            print("Soy mujer")

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