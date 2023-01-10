from PySide6.QtCore import Signal, QObject


class ObservableProperty(QObject):
    valueChanged = Signal((str), name="valueChanged")

    def __init__(self, prop) -> None:
        super().__init__()
        self.prop = prop
        self.set(prop)
        pass

    def get(self):
        return self.prop

    def set(self, value):
        if value != self.prop:
            self.prop = value
            self.valueChanged.emit(self.prop)
            return
        return
