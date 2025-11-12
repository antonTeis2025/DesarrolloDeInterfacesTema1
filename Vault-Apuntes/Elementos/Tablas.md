Añadimos en QtDesigner un **Table Widget**.

Con **Click derecho > Edit Fields** editamos los nombres de las columnas
![[Pasted image 20251112200848.png]]

---
### Insertar Datos

Para insertar los datos de los campos de texto a la tabla, primero hacemos un metodo que cargue todos esos datos a un **diccionario**, desde el que los trataremos facilmente.
```python
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
        # Eliminamos los duplicados de los métodos de pago (las checkboxes dan ese problema)  
        var.pay = set(var.pay)  
        for i in var.pay:  
            # Añadimos al diccionario cliente los metodos de pago  
            cliente.append(i)  
        # Añadimos la variable global que guarda su sexo  
        cliente.append(sex)  
        # Probamos a imprimir el cliente para ver si está to bien  
        print(cliente)  
        # Limpiamos la lista de pagos  
        var.pay = []  
        # Devolvemos el diccionario con los datos del cliente  
        return cliente  
    except Exception as error:  
        print("Error ", error)
```

Esta funcion debería devolver una lista como esta:
`['00000000T', 'Apellidos', 'Nombre', '12/11/2025', 'Lugo', 'Tarjeta', 'Hombre']`
	El formato es una puta basura pero eso es cosa de Juan Carlos, yo soy como los monos tecleando que solo hacen lo que les dicen que tienen que hacer.

Ahora, hacemos la función que insertará los datos a la tabla, que son solo los primeros 3.
```python
def insertarCliente():  
    try:  
        # Creamos un diccionario vacio que será el que insertemos en la tabla  
        insertar = []  
        # Conseguimos la lista de datos del cliente  
        cliente = Customers.datosCliente()  
        # Insertamos los 3 primeros datos de cliente (DNI, apellidos y nombre) al diccionario que se insertara  
        insertar.append(cliente[0])  
        insertar.append(cliente[1])  
        insertar.append(cliente[2])  
  
        row = 0 # Posicion de la fila para que inserte arriba de to  
        column = 0 # Posicion de la columna  
        var.ui.tablaClientes.insertRow(row) # Añade una fila a la tabla  
        for registro in insertar:  
            # cada celda tiene una posición (fila, columna) y cargamos el dato  
            cell = QtWidgets.QTableWidgetItem(registro) # Creamos un objeto tipo celda de QTable  
            var.ui.tablaClientes.setItem(row, column, cell) # Escribe el dato cell en la posicion row, column  
            column+=1 # Suma 1 para ir a la siguiente columna a insertar el siguiente registro  
        print(insertar)  
  
    except Exception as error:  
        print("Error ", error)
        
```

Solo resta **asignar el botón aceptar con la función insertarCliente**.
```python
# Asignamos al boton de aceptar la funcion insertarCliente  
var.ui.botAceptar.clicked.connect(clients.Customers.insertarCliente)
```

---
### Cargar datos de la tabla

Para cargar los datos que tenemos en la tabla, crearemos una función **cargarCliente**.
```python
def cargarCliente():  
    try:  
        # Cargamos a la variable fila los valores de la fila seleccionada de la tabla  
        # !! Esta fila es una lista de objetos tipo QTableWidgetItem, no de strings        fila = var.ui.tablaClientes.selectedItems()  
        # Creamos un diccionario con los widgets line edit a los que cargaremos los datos  
        camposCliente = [var.ui.txtDniCli, var.ui.txtApelidosCli, var.ui.txtNombreCli]  
        if fila: # Si la fila no está vacía...  
            # Extraemos el texto de cada objeto del diccionario            fila = [dato.text() for dato in fila]  
        # Imprimimos la fila para ver que to esté bien  
        print(fila)  
        i = 0  
        # Recorremos la lista de los campos cliente con un indice i  
        for i, dato in enumerate(camposCliente):  
            # Asignamos a cada campo su dato correspondiente de la lista de datos  
            dato.setText(fila[i])  
  
    except Exception as e:  
        print("Error ", e)
```

Configuraremos un evento para la tabla para que con hacer click sobre un registro, se carguen a los campos todos los datos.
```python
    def cargarCliente():
        try:
            # Cargamos a la variable fila los valores de la fila seleccionada de la tabla
            # !! Esta fila es una lista de objetos tipo QTableWidgetItem, no de strings
            fila = var.ui.tablaClientes.selectedItems()
            # Creamos un diccionario con los widgets line edit a los que cargaremos los datos
            camposCliente = [var.ui.txtDniCli, var.ui.txtApelidosCli, var.ui.txtNombreCli]
            if fila: # Si la fila no está vacía...
                # Extraemos el texto de cada objeto del diccionario
                fila = [dato.text() for dato in fila]
            # Imprimimos la fila para ver que to esté bien
            print(fila)
            i = 0
            # Recorremos la lista de los campos cliente con un indice i
            for i, dato in enumerate(camposCliente):
                # Asignamos a cada campo su dato correspondiente de la lista de datos
                dato.setText(fila[i])

        except Exception as e:
            print("Error ", e)
```