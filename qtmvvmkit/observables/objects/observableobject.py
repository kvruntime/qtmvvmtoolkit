from PyQt6.QtCore import QObject


class ObservableObject(QObject):
    def __init__(self):
        super().__init__()
        self.page_title: str = "ViewModel"
        pass
