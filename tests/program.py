import qdarktheme

qdarktheme.load_stylesheet()
from app import App
from appshell import AppShell


class Program:
    def __init__(self) -> None:
        self.app = App(AppShell)
        self.app.configureApplication("testapp", "1.0.0", 500)
        self.app.centerWindow()
        self.app.setStyleSheet(qdarktheme.load_stylesheet("light"))
        self.app.launch()

    pass
