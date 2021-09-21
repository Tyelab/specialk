from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMenu, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        # Super gives access to parent class utilities
        super().__init__()
        self.setWindowTitle("Scalpel!")
        self.setWindowIcon(QIcon("ketamine.png"))

        self.setGeometry(0, 0, 600, 600)
        self.setStyleSheet("background-color:blue")
        self.setWindowOpacity(0.90)

        # Add horizontal layout for GUI
        '''
        hbox = QHBoxLayout()

        btn1 = QPushButton("ClickOne")
        btn2 = QPushButton("click2")
        btn3 = QPushButton("click3")
        btn4 = QPushButton("click4")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        # hbox.addSpacing(100)
        hbox.addStretch(5)

        # Buttons aligned horizontally
        self.setLayout(hbox)
        '''

        # Textboxes
        '''
        line_edit = QLineEdit(self)
        line_edit.setGeometry(0, 0, 200, 100)
        line_edit.setFont(QFont("Times", 8, QFont.Weight.Bold))
        line_edit.setStyleSheet("background-color:white")
        line_edit.setPlaceholderText("Please enter subject_id")
        # Determines if you can write into the line_edit box
        # line_edit.setEnabled(False)
        # Hides text entered as in a password!
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        '''

        # Getting an image into a label
        '''
        label = QLabel(self)

        pixmap = QPixmap("ketamine.png")
        label.setPixmap(pixmap)
        '''

        # Getting a movie into a label
        '''
        label = QLabel(self)
        movie = QMovie("scalpelgif.gif")
        movie.setSpeed(100)
        label.setMovie(movie)
        movie.start()
        '''

        # Making a button
        '''
        self.create_button()

    def create_button(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(0, 0, 130, 130)
        btn.setFont(QFont("Times", 15, QFont.Weight.Bold))
        btn.setIcon(QIcon("ketamine.png"))
        btn.setIconSize(QSize(36, 36))

        menu = QMenu()
        menu.addAction("Copy")
        menu.setStyleSheet("background-color:green")
        menu.setFont(QFont("Times", 15, QFont.Weight.Bold))
        menu.addAction("cut")
        menu.addAction("paste")

        btn.setMenu(menu)
        '''
        # self.setStyleSheet(stylesheet)
        # self.create_widgets()

    # def create_widgets(self):
    #     button = QPushButton("Click me!", self)
    #     button.setGeometry(100, 100, 100, 100)
    #     button.setStyleSheet("background-color:red")
    #     button.setIcon(QIcon("ketamine.png"))
    #     button.clicked.connect(self.clicked_button)

    #     self.label = QLabel("My Label", self)
    #     self.label.setGeometry(100, 200, 100, 100)
    #     self.label.setStyleSheet("background-color:green")
    #     self.label.setFont(QFont("Times New Roman", 15))
    #     self.label.setStyleSheet("color:red")
    #     self.label.setNum(15)
    #     self.label.clear()

    # def clicked_button(self):
    #     self.label.setText("Text is changed!")
    #     self.label.setStyleSheet("background-color:red")



app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
