import sys
from PyQt6.QtWidgets import QApplication
from .AppShell import AppShell

class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.appShell=AppShell()
        pass

    def launch(self):
        self.appShell.show()
        sys.exit(self.exec())