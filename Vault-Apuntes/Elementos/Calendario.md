Primero, creamos un campo para poner fecha con un botón al lado.
![[Pasted image 20251112184409.png]]
El calendario en QtDesigner será una ventana tipo **Dialog without buttons**, a la que añadiremos un **Widget Calendario**. Quedará así.
![[Pasted image 20251112183218.png]]

---
Para implementarlo a código, primero compilamos el archivo .ui, y ya teniéndolo, crearemos una clase DialogCalendar dentro del propio archivo python compilado. En el constructor de esta clase, vamos a definir que cuando **se abra el calendario, esté en la fecha actual por defecto**.
```python
class DialogCalendar(QtWidgets.QDialog):  
    def __init__(self):  
        super(DialogCalendar, self).__init__()  
        # Definimos la variable global dlgcalendar como Ui_Dialog, que es la clase que crea qt desinger
        var.dlgcalendar = Ui_Dialog()  
        # Inicializamos la interfaz
        var.dlgcalendar.setupUi(self)
        # Creamos variables para el día, més y año  
        diaactual = datetime.datetime.now().day  
        mesactual = datetime.datetime.now().month  
        anoactual = datetime.datetime.now().year  
        # Con el método setSelectedDate de calendarWidget, establecemos la fecha mostrada a la de hoy. Hay que pasarsela convertida a tipo QDate
        var.dlgcalendar.calendarWidget.setSelectedDate(QtCore.QDate(
	        anoactual,
	        mesactual,
	        diaactual
	    ))
	    # Hacemos que cuando se clickee sobre el, cargue la fecha al line edit con el método cargarFecha
        var.dlgcalendar.calendarWidget.clicked.connect(events.Eventos.cargarFecha)
```
Ahora, **creamos los siguientes eventos** para el calendario:
```python
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
```
Por último, en Main, **instanciamos la ventana del calendario** y **asignamos el evento al botón**:
```python
# Cargamos el objeto DialogCalendar a una variable global  
var.dlgcalendar = calendar.DialogCalendar()
# Al pulsar el boton del calendario, se abre el widged almacenado en dlgCalendar  
var.ui.botCalendar.clicked.connect(events.Eventos.abrirCalendar)
```