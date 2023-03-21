from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal
import typing


class ObservableFloatProperty(QObject):
    valueChanged = pyqtSignal(float, name="valueChanged")

    def __init__(self, prop: float=0) -> None:
        super().__init__()
        self.prop: float = prop
        self.set(prop)
        pass

    def get(self):
        return self.prop

    def set(self, value: float):
        if value != self.prop:
            self.prop = value
            self.valueChanged.emit(self.prop)
        return
