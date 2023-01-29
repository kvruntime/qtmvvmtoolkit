from  PyQt6.QtWidgets import QMainWindow
from qtqtmvvmkit.widgets.navigationpage import NavigationPage

class AppShell(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(NavigationPage())
        pass