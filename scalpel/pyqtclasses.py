from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QApplication, QWidget, QPushButton, QLabel, QMenu, QLineEdit, QHBoxLayout
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
        # self.setStyleSheet("background-color:blue")
        self.setWindowOpacity(1)

        self.create_widget()

    # Every widget gives a signal when an event is applied and each signal takes a slot/method
    def create_widget(self):
        hbox = QHBoxLayout()

        btn1 = QPushButton("Change Text")
        self.label = QLabel("Default Text")
        # Connect method
        btn1.clicked.connect(self.clicked_btn)

        hbox.addWidget(btn1)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    # Signal for button
    def clicked_btn(self):
        self.label.setText("New text!")

        self.label.setFont(QFont("Times", 15))

        self.label.setStyleSheet("color:red")




        # Make Grid Layout
        '''
        grid = QGridLayout()

        btn1 = QPushButton("one")
        btn2 = QPushButton("two")
        btn3 = QPushButton("three")
        btn4 = QPushButton("four")
        btn5 = QPushButton("five")
        btn6 = QPushButton("six")
        btn7 = QPushButton("seven")
        btn8 = QPushButton("eight")

        # Widget, row/column
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)
        '''







        # Add vertical layout for GUI
        '''
        vbox = QVBoxLayout()

        btn1 = QPushButton("Click one")
        btn2 = QPushButton("Click 2")
        btn3 = QPushButton("Click 3")
        btn4 = QPushButton("Click 4")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addSpacing(100)
        vbox.addStretch(5)

        self.setLayout(vbox)
        '''


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
