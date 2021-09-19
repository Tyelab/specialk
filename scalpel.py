# Form implementation generated from reading ui file 'scalpel.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("QWidget {\n"
"\n"
"background-color: rgb(85, 170, 255)\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"background-color: \"red\"\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"\n"
"color: \"green\"\n"
"\n"
"}\n"
"")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked_button)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 110, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Modern")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def clicked_button(self):
        self.label.setText("Changed!")
        self.label.setStyleSheet("background-color:yellow")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scalpel!"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
