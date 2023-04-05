import sys
import typing
from PyQt6.QtWidgets import QApplication, QMainWindow
import context
context.__file__
from qtmvvmtoolkit.widgets import BaseApp


class App(BaseApp):
    def __init__(self, appshell: typing.Type[QMainWindow]):
        super().__init__(sys.argv)
        self.appShell = appshell()
        self.appShell.show()
        pass

    def launch(self):
        sys.exit(self.exec())
