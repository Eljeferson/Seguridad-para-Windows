# Seguridad para Windows 

Este proyecto es una herramienta diseñada para mejorar la seguridad de sistemas operativos Windows mediante la configuración automática de políticas básicas de seguridad, utilizando Python y un script complementario en `.bat`.

## **Características**
- Activación del Firewall de Windows.
- Configuración de políticas de contraseñas seguras.
- Deshabilitación de servicios considerados inseguros.
- Generación de un reporte de seguridad con información relevante del sistema.

## **Requisitos**
- **Sistema Operativo:** Windows 10 o superior.
- **Software necesario:**
  - Python 3.x
  - Librerías de Python: `PyQt5`
  - Permisos de administrador para ejecutar scripts.

## **Archivos**
- **`SeguridadWindows.py`**: Script principal en Python para la configuración y generación del reporte.
- **`SeguirdadWindws.bat`**: Script para ejecutar el programa con permisos de administrador.
- **`reporte_seguridad.txt`**: Archivo que contiene el reporte generado con el estado de seguridad del sistema.

## **Instrucciones de Uso**
1. Asegúrate de tener Python instalado junto con la librería `PyQt5`. Instálalo con:
   ```bash
   pip install pyqt5
   ```
2. Ejecuta el archivo `.bat` para iniciar la herramienta con permisos de administrador.
3. Utiliza la interfaz gráfica para seleccionar las acciones de seguridad que deseas aplicar.
4. Revisa el reporte generado en la carpeta de descargas (`reporte_seguridad.txt`).

## **Advertencia**
Este programa debe ejecutarse **únicamente** en sistemas donde tengas permiso administrativo y conocimiento de las configuraciones realizadas.

---

¡Contribuye a un entorno más seguro con esta herramienta!
