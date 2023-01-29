from qdarktheme import load_stylesheet
from .App import App
class Program:
    def __init__(self) -> None:
        self.app = App()
        self.app.setStyleSheet(load_stylesheet("light"))
        self.app.launch()
    pass
