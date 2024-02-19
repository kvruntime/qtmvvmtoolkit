import context
from pages.homepage import HomePage
from pages.pageuser import PageUser

context.__file__

from PyQt6.QtWidgets import QMainWindow, QTabWidget


class AppShell(QMainWindow):
    def __init__(self):
        super().__init__()
        self.outlet = QTabWidget(self)
        self.setCentralWidget(self.outlet)

        self.outlet.addTab(HomePage(), "HomePage")
        self.outlet.addTab(PageUser(), "UserPage")
        pass
