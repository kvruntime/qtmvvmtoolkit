from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal
import typing


class ObservableIntProperty(QObject):
    valueChanged = pyqtSignal(int, name="valueChanged")

    def __init__(self, prop: int = 0) -> None:
        super().__init__()
        self.prop: int = prop
        self.set(prop)
        pass

    def get(self):
        return self.prop

    def set(self, value: int):
        if value != self.prop:
            self.prop = value
            self.valueChanged.emit(self.prop)
        return
