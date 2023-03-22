import typing
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QLabel, QComboBox, QPushButton, QToolButton
)
from qtmvvmkit.observables.properties import (
    ObservableProperty, ObservableIntProperty, ObservableFloatProperty
)


class BindableObject(QObject):
    def __init__(self, parent: typing.Optional[QWidget] = None):
        super().__init__(parent)
        pass
    
    def binding(self, widget:QWidget, prop:str, observable:ObservableProperty)->None:
        # Implement this method
        return None

    def bind_entry_to_str(self, prop: ObservableFloatProperty, widget: QLineEdit) -> None:
        prop.valueChanged[str].connect(widget.setText)
        widget.textChanged.connect(prop.set)
        return None
    
    def bind_entry_to_int(self, prop:ObservableIntProperty, widget:QLineEdit):
        prop.valueChanged.connect(lambda value:widget.setText(str(value)))
        widget.textChanged.connect(lambda value: prop.set(int(value)))
        return None

    def bind_label(self, prop: ObservableProperty, widget: QLabel) -> None:
        prop.valueChanged[str].connect(lambda value: widget.setText(str(value)))
        
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
