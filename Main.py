import sys
from turtledemo.nim import COLOR

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget
from OtraVentana import OtraWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana Principal")
        self.setFixedSize(600, 400)

        palete = self.palette()
        palete.setColor(QPalette.ColorRole.Window, QColor("green")) #cambiamos el color con la variabñe
        self.setPalette(palete)

        self.button_pulsar_oculta_ventana = QPushButton("Otra ventana")
        self.button_pulsar_oculta_ventana.clicked.connect(self.cambioVentana)

        caja = QVBoxLayout()
        caja.addWidget(self.button_pulsar_oculta_ventana)

        container = QWidget()
        container.setLayout(caja)
        self.setCentralWidget(container)

        self.ventanaSecundaria = None

    def cambioVentana(self):
        if self.ventanaSecundaria is None:
            self.ventanaSecundaria = OtraWindow(self)

        self.ventanaSecundaria.show()
        self.hide()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = MainWindow()
    fiestra.show()
    sys.exit(aplicacion.exec())