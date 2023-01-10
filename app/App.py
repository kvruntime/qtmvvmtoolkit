import sys
from PyQt6.QtWidgets import QApplication
from .AppShell import AppShell

class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.appShell=AppShell()
        self.appShell.show()
        pass

    def launch(self):
        sys.exit(self.exec())