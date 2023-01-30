from PyQt6.QtCore import QObject


class ObservableObject(QObject):
    def __init__(self):
        super().__init__()
        self.title: str = "ViewModel"
        pass
