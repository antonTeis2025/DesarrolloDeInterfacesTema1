from var import rbtsexo
from window import *
import confirmacion_salida
import sys
import var, events, clients, calendar # importacion de los ficheros locales
import datetime




class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        # Cargamos el objeto DialogCalendar a una variable global
        var.dlgcalendar = calendar.DialogCalendar()
        # Cargamos el menú de salir a una variable global
        var.avisosalir = confirmacion_salida.Ui_Dialog()
        # Creamos un QtDialog, para que salga como ventana de confirmacion
        var.dlgSalir = QtWidgets.QDialog()
        # Hacemos el setupUI con el dialogo como argumento
        var.avisosalir.setupUi(var.dlgSalir)

        # --- Conexion con los eventos ---

        # Carga de datos para la combobox provincia
        events.Eventos.cargaProvincias()

        # Eventos botones

        # Boton que cuando se le da a salir limpia todos los datos
        var.ui.botSalir.clicked.connect(clients.Customers.limpiarCliente)
        # Boton que cuando se le da a salir en el menu ejecuta Salir
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        # Asignamos los dos radioButtons a una misma variable tipo lista
        var.rbtsexo = (var.ui.rbtHombre, var.ui.rbtMujer)
        for i in var.rbtsexo:
            # Les decimos a todos que cuando haya un cambio, se ejecute selSexo
            i.toggled.connect(clients.Customers.selSexo)
        # Guardamos todos los checkbox en una lista
        var.cbpago = (var.ui.cbTarjeta, var.ui.cbEfectivo, var.ui.cbTransferencia)
        for i in var.cbpago:
            # Hacemos que por cada actualización, se ejecute selPago
            i.stateChanged.connect(clients.Customers.selPago)
        # Al pulsar el boton del calendario, se abre el widged almacenado en dlgCalendar
        var.ui.botCalendar.clicked.connect(events.Eventos.abrirCalendar)

        # Eventos editando

        # Comprobar el DNI cada vez que se deja de escribir
        var.ui.txtDniCli.editingFinished.connect(clients.Customers.checkDni)
        # Cada vez que se edite ComboBox provincia, ejecuta selProvincia
        var.ui.comboBoxProvincias.activated[str].connect(clients.Customers.selProvincia)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())