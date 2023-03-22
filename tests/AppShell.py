import context
context.__file__

from  PyQt6.QtWidgets import QMainWindow, QWidget

class AppShell(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QWidget())
        pass