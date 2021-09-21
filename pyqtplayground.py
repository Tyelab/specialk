# Team Specialk Surgery Metadata Generation
# Jeremy Delahanty September 2021

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# from ruamel.yaml import YAML

from pathlib import Path

server_basepath = Path("X:/")

app = QApplication(sys.argv)

# 3 types of window to use: Q widget, q main window, q dialog

window = QMainWindow()
window.statusBar().showMessage("Hello, Surgeon! Welcome to Scalpel")
window.menuBar().addMenu("Test")

window.show()

sys.exit(app.exec())
