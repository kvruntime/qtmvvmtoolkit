from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget, QLineEdit, QLabel
from mvvmkit.observables.observableproperty import ObservableProperty


class BindableView(QObject):
    def __init__(self):
        super().__init__()
        pass

    def bind(self, prop: ObservableProperty, widget: QWidget):
        match widget:
            case QLineEdit():
                prop.valueChanged.connect(widget.setText)
                widget.textChanged.connect(prop.set)  # type:ignore
                return

            case QLabel():
                prop.valueChanged.connect(widget.setText)

            case _:
                raise Exception("Not applicable")
        pass
