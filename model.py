from PySide6.QtCore import Signal, Property, Slot, QObject, Qt
from PySide6.QtWidgets import QPushButton, QLineEdit


entry = QLineEdit()


class QModel(QObject):
    valueChanged = Signal((str), (int),
                          name="valueChanged",
                          arguments="value")

    def __init__(self):
        super().__init__()

        self.valueChanged.emit("valueChanged Emission")
        self.valueChanged.emit(9)

        self.valueChanged.connect(self.on_value_changed)
        self.valueChanged.disconnect(self.on_value_changed)

        pass

    def get(self):
        return

    def set(self, value):
        self.valueChanged.emit(value)
        return

    @Slot(str)
    @Slot(int)
    def on_value_changed(self, value):
        print(f"value emitted: {value}")
        return None
