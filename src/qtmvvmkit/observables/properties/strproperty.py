from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal
import typing


class ObservableStrProperty(QObject):
    valueChanged = pyqtSignal(str, name="valueChanged")

    def __init__(self, prop: str = "") -> None:
        super().__init__()
        self.prop: str = prop
        self.set(prop)
        pass

    def get(self):
        return self.prop

    def set(self, value: str):
        if value != self.prop:
            self.prop = value
            self.valueChanged.emit(self.prop)
        return
