import subprocess
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit, QMessageBox

def es_administrador():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def activar_firewall():
    try:
        subprocess.run("netsh advfirewall set allprofiles state on", check=True, shell=True)
        agregar_texto("✅ Firewall activado correctamente.")
    except subprocess.CalledProcessError:
        agregar_texto("❌ Error al activar el Firewall.")

def configurar_politicas_contrasena():
    try:
        subprocess.run("net accounts /minpwlen:12 /maxpwage:30", check=True, shell=True)
        agregar_texto("✅ Políticas de contraseñas configuradas.")
    except subprocess.CalledProcessError:
        agregar_texto("❌ Error al configurar las políticas de contraseñas.")

def deshabilitar_servicios_inseguros():
    servicios = ["wuauserv"]  # Agrega otros servicios inseguros si es necesario
    for servicio in servicios:
        try:
            subprocess.run(f"sc config {servicio} start= disabled", check=True, shell=True)
            agregar_texto(f"✅ Servicio {servicio} deshabilitado.")
        except subprocess.CalledProcessError:
            agregar_texto(f"❌ Error al deshabilitar el servicio {servicio}.")

def generar_reporte():
    try:
        
        ruta_descargas = r'C:\Users\USER\Downloads\Seguridad para Windows\reporte_seguridad.txt'

        reporte = []
        
        firewall_status = subprocess.getoutput("netsh advfirewall show allprofiles state")
        reporte.append(f"Estado del Firewall:\n{firewall_status}\n")
        
        try:
            admins = subprocess.getoutput("net localgroup Administrators")
        except Exception as e:
            admins = f"❌ Error al obtener los usuarios administradores: {e}"

        admins = subprocess.getoutput("net localgroup Administradores") 
        reporte.append(f"Usuarios administradores:\n{admins}\n")

        with open(ruta_descargas, "w", encoding="utf-8") as archivo:
            archivo.write("".join(reporte))  
        agregar_texto("✅ Reporte generado: reporte_seguridad.txt")
    except Exception as e:
        agregar_texto(f"❌ Error al generar el reporte: {e}")

def agregar_texto(mensaje):
    ventana.output_area.append(mensaje)


class VentanaSeguridad(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Herramienta de Seguridad para Windows")
        self.setGeometry(100, 100, 600, 400)

        if not es_administrador():
            QMessageBox.critical(self, "Error de Permisos", "Este script debe ejecutarse como administrador.")
            self.close()

        layout = QVBoxLayout()

        titulo = QLabel("Herramienta de Seguridad para Windows")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        boton_firewall = QPushButton("Activar Firewall")
        boton_firewall.clicked.connect(activar_firewall)
        layout.addWidget(boton_firewall)

        boton_contrasenas = QPushButton("Configurar Contraseñas")
        boton_contrasenas.clicked.connect(configurar_politicas_contrasena)
        layout.addWidget(boton_contrasenas)

        boton_servicios = QPushButton("Deshabilitar Servicios")
        boton_servicios.clicked.connect(deshabilitar_servicios_inseguros)
        layout.addWidget(boton_servicios)

        boton_reporte = QPushButton("Generar Reporte")
        boton_reporte.clicked.connect(generar_reporte)
        layout.addWidget(boton_reporte)

        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        boton_cerrar = QPushButton("Cerrar")
        boton_cerrar.clicked.connect(self.close)
        layout.addWidget(boton_cerrar)

        self.setLayout(layout)


def main():
    global ventana  
    app = QApplication([])
    ventana = VentanaSeguridad()
    ventana.show()
    app.exec_()


if __name__ == "__main__":
    main()
