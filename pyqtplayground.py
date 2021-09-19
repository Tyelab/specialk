# Team Specialk Surgery Metadata Generation
# Jeremy Delahanty September 2021

from PyQt6.QtWidgets import QApplication, QWidget
import sys

from ruamel.yaml import YAML

from pathlib import Path

server_basepath = Path("X:/")

app = QApplication(sys.argv)

# 3 types of window to use: Q widget, q main window, q dialog

window = QWidget()

window.show()

sys.exit(app.exec())
