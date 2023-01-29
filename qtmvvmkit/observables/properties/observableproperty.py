from PyQt6.QtCore import pyqtSignal as Signal, QObject
import typing


class ObservableProperty(QObject):
    valueChanged = Signal((str), name="valueChanged")

    def __init__(self, prop) -> None:
        super().__init__()
        self.prop: typing.Any
        self.set(prop)
        pass

    def get(self):
        return self.prop

    def set(self, value):
        if value != self.prop:
            self.prop = value
            self.valueChanged.emit(self.prop)
        return
