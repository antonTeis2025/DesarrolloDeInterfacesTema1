Se encarga de gestionar los eventos. Cuando el proyecto crece, se separa en varios ficheros diferentes para agrupar las funciones por categoría.

Definimos un evento en la clase eventos:
```python
class Eventos():  
  
    def Saludo():  
  
        try:  
            print("BOTON PRESIONADO")  
        except Exception as error:  
            print("Error ", error)
```
Hacemos un trigger en main para que cuando se pulse un boton, se ejecute el evento.
```python
class Main(QtWidgets.QMainWindow):  
    def __init__(self):  
        super(Main, self).__init__()  
        var.ui = Ui_MainWindow()  
        var.ui.setupUi(self)  
  
        # --- Conexion con los eventos ---  
        
        # ui (MainWindow) > botonPrueba (label del boton) > clicked.connect(Funcion)
        var.ui.botonPrueba.clicked.connect(events.Eventos.Saludo)
```
---
Para **llamar a los eventos**:
- **Terminada la edición de un campo de texto**: ``elemento.editingFinished.connect(funcion)``
- 