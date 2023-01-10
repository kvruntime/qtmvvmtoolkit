from  PyQt6.QtWidgets import QMainWindow

from app.pages.PageNav import PageNav

class AppShell(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pageNav = PageNav()
        self.setCentralWidget(self.pageNav)
        pass