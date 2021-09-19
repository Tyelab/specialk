from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scalpel!")
        self.setWindowIcon(QIcon("ketamine.png"))

        self.setGeometry(0, 0, 600, 600)

        stylesheet = (
            'background-color:red'
        )

        # self.setStyleSheet(stylesheet)
        self.create_widgets()

    def create_widgets(self):
        button = QPushButton("Click me!", self)
        button.setGeometry(100, 100, 100, 100)
        button.setStyleSheet("background-color:red")
        button.setIcon(QIcon("ketamine.png"))
        button.clicked.connect(self.clicked_button)

        self.label = QLabel("My Label", self)
        self.label.setGeometry(100, 200, 100, 100)
        self.label.setStyleSheet("background-color:green")
        self.label.setFont(QFont("Times New Roman", 15))

    def clicked_button(self):
        self.label.setText("Text is changed!")
        self.label.setStyleSheet("background-color:red")



app = QApplication([])

window = Window()

window.show()

sys.exit(app.exec())
