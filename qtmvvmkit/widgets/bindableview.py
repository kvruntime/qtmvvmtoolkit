import typing
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import (QWidget, QLineEdit, QLabel, QComboBox)
from qtmvvmkit.observables.properties.observableproperty import ObservableProperty


class BindableView(QObject):
    def __init__(self):
        super().__init__()
        pass

    def bind_entry(
        self,
        prop: ObservableProperty,
        widget: QLineEdit
    ):
        prop.valueChanged.connect(widget.setText)
        widget.textChanged.connect(prop.set)
        return None

    def bind_label(
            self,
            prop: ObservableProperty,
            widget: QLabel
    ):
        prop.valueChanged.connect(lambda value: widget.setText(str(value)))
        return None

    def bind_combobox_items(
        self,
        prop: ObservableProperty,
        widget: QComboBox
    ) -> None:
        prop.valueChanged.connect(widget.addItems)
        return None

    def bind_command(
        self,
        button: typing.Union[QPushButton, QToolButton],
        command: typing.Callable[[], None]
    ):
        button.clicked.connect(lambda: command())
        return None
