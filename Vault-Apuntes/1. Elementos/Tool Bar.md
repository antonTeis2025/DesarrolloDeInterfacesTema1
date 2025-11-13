Además de las acciones del menú, podemos crear una toolbar para poner acciones de forma mucho más organizada. 

Haremos **click derecho > Add toolbar**
![[Pasted image 20251113214705.png]]

En la toolbar, abajo aparecerá el action editor, donde podemos crear acciones para asignarlas al codigo:

![[Pasted image 20251113214903.png]]

Al crear una nueva accion, podemos asignarle **Nombre, Icono y atajo de teclado**:

![[Pasted image 20251113214933.png]]

Si lo **arrastramos a la toolbar** tendremos acceso a ella.

---
Para tener acceso desde el código, haremos como con cualquier accion normal, con:
```python
accion.triggered.connect()
```