# Semana 02: entorno de trabajo

Desde la raíz del repositorio creé el entorno con `python -m venv venv`.
En PowerShell lo activo con `.\venv\Scripts\Activate.ps1` y confirmo el prefijo `(venv)`.
Para salir del entorno uso `deactivate`.
Con el entorno activo instalé la dependencia con `python -m pip install matplotlib`.
Después generé las versiones exactas con `python -m pip freeze > requirements.txt`.
Otra persona puede crear su propio entorno en la raíz y activarlo.
Luego debe ejecutar `python -m pip install -r requirements.txt` para reproducirlo.
La carpeta `venv/` está en `.gitignore` y no se sube al repositorio.