import typing

from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import (
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QWidget,
)

from .observableproperty import ObservableProperty, ComputedObservableProperty
from .boolproperty import ObservableBoolProperty, ComputedObservableBoolProperty
from .floatproperty import ObservableFloatProperty, ComputedObservableFloatProperty
from .intproperty import ObservableIntProperty, ComputedObservableIntProperty
from .relayableproperty import RelayableProperty
from .strproperty import ObservableStrProperty, ComputedObservableStrProperty


class BindableObject(QObject):
    def __init__(self, parent: typing.Optional[QWidget] = None):
        super().__init__(parent)
        pass

    def binding(
        self, widget: QWidget, prop: str, observable: ObservableProperty
    ) -> None:
        # Implement this method
        return None

    # Relayable Property
    def bind_relayable_property(
        self, value: RelayableProperty, function: typing.Callable[..., None]
    ) -> None:
        value.relayed.connect(lambda: function())
        return None

    def relaying(
        self, value: RelayableProperty, function: typing.Callable[..., None]
    ) -> None:
        value.relayed.connect(lambda: function())
        return None

    def bind_lineedit(self, prop: ObservableStrProperty, widget: QLineEdit) -> None:
        prop.valueChanged.connect(widget.setText)
        widget.textChanged.connect(prop.set)
        prop.valueChanged.emit(prop.get())
        return None

    def bind_lineedit_to_int(self, prop: ObservableIntProperty, widget: QLineEdit):
        prop.valueChanged.connect(lambda value: widget.setText(str(value)))
        prop.valueChanged.emit(prop.get())
        return None

    def bind_lineedit_to_float(self, prop: ObservableFloatProperty, widget: QLineEdit):
        prop.valueChanged.connect(lambda value: widget.setText(str(round(value, 3))))
        prop.valueChanged.emit(prop.get())
        return None

    def bind_label(self, prop: ObservableStrProperty, widget: QLabel) -> None:
        prop.valueChanged.connect(widget.setText)
        prop.valueChanged.emit(prop.get())
        return None

    def bind_label_to_int(self, prop: ObservableIntProperty, widget: QLabel) -> None:
        prop.valueChanged.connect(lambda value: widget.setText(str(value)))
        prop.valueChanged.emit(prop.get())
        return None

    def bind_combobox_items(self, prop: ObservableProperty, widget: QComboBox) -> None:
        prop.valueChanged.connect(widget.addItems)
        return None

    # QSPINBOX
    def bind_spinbox(
        self,
        prop: typing.Union[ObservableIntProperty, ComputedObservableIntProperty],
        widget: QSpinBox,
    ):
        prop.valueChanged.connect(widget.setValue)
        widget.valueChanged.connect(prop.set)
        prop.valueChanged.emit(prop.get())
        return None

    # QDoubleSpinBox
    def bind_dspin(self, value: ObservableFloatProperty, widget: QDoubleSpinBox):
        value.valueChanged.connect(widget.setValue)
        widget.valueChanged.connect(value.set)
        value.valueChanged.emit(value.get())
        return None

    def bind_dspin_percent(self, prop: ObservableFloatProperty, widget: QDoubleSpinBox):
        prop.valueChanged.connect(lambda value: widget.setValue(value * 100))
        widget.valueChanged.connect(lambda value: prop.set(value / 100))
        prop.valueChanged.emit(prop.get())
        return None

    # QPushButton
    def bind_button_command(
        self, button: QPushButton, command: typing.Callable[[], None]
    ):
        button.clicked.connect(lambda: command())
        return None

    def bind_button_state(self, prop: ObservableBoolProperty, widget: QPushButton):
        prop.valueChanged.connect(lambda value: widget.setEnabled(value))
        prop.valueChanged.emit(prop.get())
        return None

    # Actions
    # def bind_action_command(self, action:QtGui.QAction, function:typing.Callable)->None:
    #     action.triggered.connect(lambda: function())
    #     return None
