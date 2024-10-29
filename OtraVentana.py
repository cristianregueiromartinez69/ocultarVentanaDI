from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget

class OtraWindow(QMainWindow):
    def __init__(self, ventana_principal):
        super().__init__()

        self.setWindowTitle("Ventana Secundaria")
        self.setFixedSize(600, 400)

        palete = self.palette()
        palete.setColor(QPalette.ColorRole.Window, QColor("pink"))
        self.setPalette(palete)

        self.ventana_principal = ventana_principal

        self.button_pulsar_oculta_ventana = QPushButton("volver")
        self.button_pulsar_oculta_ventana.clicked.connect(self.cambioVentana)

        caja = QVBoxLayout()
        caja.addWidget(self.button_pulsar_oculta_ventana)

        container = QWidget()
        container.setLayout(caja)
        self.setCentralWidget(container)

    def cambioVentana(self):
        self.ventana_principal.show()
        self.hide()