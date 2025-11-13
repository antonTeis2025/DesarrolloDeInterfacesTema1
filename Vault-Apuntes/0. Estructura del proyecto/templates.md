La carpeta templates contendrá los **archivos .ui** resultantes de guardar los diseños de QT Designer.

---
Para poder usar estos diseños, es necesario **compilarlos**. Esto lo haremos con una utilidad nativa de QtDesigner: pyuic5.exe

Está por defecto instalada en ``\.venv\Scripts\pyuic5.exe``, automáticamente creada al instalar la dependencia pyqt5. 

Para compilar un .ui (XML) a un archivo python que podamos usar:
```powershell
pyuic5.exe -x window.ui -o window.py
```
